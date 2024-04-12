import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from graph import plot_average_order_amount
from graph import plot_monthly_sales
from graph import plot_percent_product_revenue
from graph import plot_sales_by_product_size
from graph import plot_sales_by_quartile
from graph import plot_top_product_revenue

def dataDisplay(data, cond):
    if "head" in cond:
        st.write("Data is show from top")
        st.write(data.head())
    if "tail" in cond:
        st.write("Data is show from bottom")
        st.write(data.tail())
    if "describe" in cond:
        st.write("Data description")
        st.write(data.describe())
    if "shape" in cond:
        st.write("Data shape")
        st.write(data.shape)
    if "info" in cond:
        st.write("Data Info")
        info = data.info()
        if info is not None:
            st.write(info)
        else:
            st.write("No information available")
    if "columns" in cond:
        st.write("Data columns name")
        st.write(data.columns)
    if "dtypes" in cond:
        st.write("Data types")
        st.write(data.dtypes)
    if "sample" in cond:
        st.write("Data sample")
        st.write(data.sample())
    if "value_counts" in cond:
        column_name = st.selectbox("Select a column to see value counts", data.columns)
        st.write("Data value counts")
        st.write(data[column_name].value_counts())
    if "isnull" in cond:
        st.write("Data isNull or not")
        st.write(data.isnull().sum())
    if "nunique" in cond:
        st.write("Data unique count")
        st.write(data.nunique().to_frame(name='Count of unique values'))
    if "unique" in cond:
        st.write("Here is what unique")
        unique_values = data.apply(lambda x: ','.join(pd.unique(x.astype(str)))).to_frame(name='Unique Values')
        st.write(unique_values)


def GraphDisplay(data,cond):
    if "heat" in cond:
        st.write(sns.heatmap(data.isnull()))
        st.write(plt.show())
    if "NetRevenue" in cond:
        st.write("Amazon India Net Revenue")
        plot_monthly_sales(data)
    if "AvgMonth" in cond:
        st.write("Amazon India Average Monthly Order")
        plot_average_order_amount(data)
    if "TopPro" in cond:
        st.write("Amazon India Top Product in Monthly")
        plot_top_product_revenue(data)
    if "perRevenue" in cond:
        st.write("Amazon India percentage product Revenue")
        plot_percent_product_revenue(data)
    if "size" in cond:
        st.write("Amazon India sales by product size")
        plot_sales_by_product_size(data)
    if "sales" in cond:
        st.write("Amazon India sales by quartile")
        plot_sales_by_quartile(data)

def DataOp(data,cond):
    if "drop" in cond:
        selected_cols = st.multiselect("Select columns to drop:", data.columns)
        dropCol = selected_cols
        if len(dropCol)>=1:
            st.write("before drop")
            st.write(data.head())
            st.write("after dropping columns :",dropCol)
            data.drop(columns=dropCol,inplace=True)
            st.write(data.head())
    if "DD" in cond:
        selected_cols = st.multiselect("Select columns to delete duplicates:", data.columns)
        deleteDuplicate = selected_cols
        if len(deleteDuplicate) >= 1:
            st.write("after deleting duplicate :",deleteDuplicate)
            data[data.duplicated(deleteDuplicate, keep=False)]
            data.drop_duplicates(deleteDuplicate,inplace=True,ignore_index=True)
            st.write(data.head())
    if "Nan" in cond:
        selected_cols = st.multiselect("Select columns to Fill NAN:", data.columns)
        fillNan = selected_cols
        if len(fillNan) >= 1:
            fill_value = st.text_input("Enter value to fill NaN:", "")
            if fill_value:
                for col in fillNan:
                    data[col].fillna(fill_value, inplace=True)
            st.write("After filling NaN: ", fillNan)
            st.write(data.head())
            st.write(data.isnull().sum())




