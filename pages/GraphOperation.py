from data import GraphDisplay
from sidebar import sidebarGraph
import streamlit as st
import pandas as pd

def clean(amazon):
    amazon.drop(columns= ['index','Unnamed: 22', 'fulfilled-by', 'ship-country', 'currency', 'Sales Channel '], inplace = True)
    amazon[amazon.duplicated(['Order ID','ASIN'], keep=False)]
    amazon.drop_duplicates(['Order ID','ASIN'],inplace = True,ignore_index=True)
    amazon['Courier Status'].fillna('unknown',inplace=True)
    amazon['promotion-ids'].fillna('no promotion',inplace=True)
    amazon[amazon['Amount'].isnull()]['Status'].value_counts(normalize=True).apply(lambda x: format(x, '.2%'))
    amazon['Amount'].fillna(0,inplace=True)
    amazon['ship-city'].fillna('unknown', inplace = True)
    amazon['ship-state'].fillna('unknown', inplace = True)
    amazon['ship-postal-code'].fillna('unknown', inplace = True)
    mapper = {'Order ID':'order_ID', 'Date':'date', 'Status':'ship_status','Fulfilment':'fullfilment',
          'ship-service-level':'service_level', 'Style':'style', 'SKU':'sku', 'Category':'product_category', 
          'Size':'size', 'ASIN':'asin', 'Courier Status':'courier_ship_status', 'Qty':'order_quantity', 
          'Amount':'order_amount_($)', 'ship-city':'city', 'ship-state':'state', 'ship-postal-code':'zip', 
          'promotion-ids':'promotion','B2B':'customer_type'}
    amazon.rename(columns=mapper, inplace =True)
    # Convert INR to USD using an exchange rate of 1 INR = 0.014 USD
    exchange_rate = 0.0120988
    amazon['order_amount_($)'] = amazon['order_amount_($)'].apply(lambda x: x * exchange_rate)
    amazon['customer_type'].replace(to_replace=[True,False],value=['business','customer'], inplace=True)
    amazon['date'] = pd.to_datetime(amazon['date'])
    amazon = amazon[(amazon['date'].dt.month != 3)]
    amazon['month'] = amazon['date'].dt.month
    month_map = { 4: 'april',5: 'may',6: 'june'}
    amazon['month'] = amazon['date'].dt.month.map(month_map)
    # Define the desired order of months
    month_order = ['april', 'may', 'june']

    # Convert the month column to a categorical data type with the desired order
    amazon['month'] = pd.Categorical(amazon['month'], categories=month_order, ordered=True)
    # Define the desired order for the 'size' column
    size_order = ['Free','XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL', '6XL']

    # Create an ordered categorical variable for the 'size' column
    amazon['size'] = pd.Categorical(amazon['size'], categories=size_order, ordered=True)

    return amazon


def main():
    data = pd.read_csv(f"EDA\sales\Amazon Sale Report.csv\Amazon Sale Report.csv")
    cond = sidebarGraph()
    data = clean(data)
    GraphDisplay(data, cond)

if __name__ == "__main__":
    main()
