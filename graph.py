import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_monthly_sales(data):
    # Group the data by month and calculate the total sales revenue
    monthly_sales = data.groupby(pd.Grouper(key='date', freq='M')).agg({'order_amount_($)': 'sum'})

    # Get latest month revenue and average quarterly revenue
    latest_month_revenue = monthly_sales.tail(1).iloc[0][0]
    avg_quarterly_revenue = monthly_sales.tail(3).head(2).mean()[0]

    # Compute percentage below average revenue for quarter
    pct_below_avg = round((1 - (latest_month_revenue / avg_quarterly_revenue)) * 100, 1)

    # Plot the monthly sales revenue
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(monthly_sales.index.strftime('%b'), monthly_sales['order_amount_($)'], color='#878787')

    # Add label above each bar with the percentage below the average revenue for the quarter
    for i, bar in enumerate(bars):
        if i == len(bars) - 1 or i < len(bars) - 2:
            continue
        month_sales = monthly_sales.iloc[i]['order_amount_($)']
        pct_below_avg = round((1 - (month_sales / avg_quarterly_revenue)) * 100, 1)
        ax.annotate(f'{pct_below_avg}% below avg.', 
                    xy=(bar.get_x() + bar.get_width()/2, bar.get_height()-7000), 
                    xytext=(0, 5), textcoords='offset points',  fontweight='bold', 
                    ha='center', va='bottom', fontsize=14)

    # Add label above the latest bar with the percentage below the average revenue for the quarter
    latest_bar = bars[-1]
    latest_month_sales = latest_bar.get_height()
    pct_below_avg = round((1 - (latest_month_sales / avg_quarterly_revenue)) * 100, 1)
    ax.annotate(f'{pct_below_avg}% below avg.', 
                xy=(latest_bar.get_x() + latest_bar.get_width()/2, latest_bar.get_height()-7000), 
                xytext=(0, 5), textcoords='offset points',  fontweight='bold',
                ha='center', va='bottom', fontsize=14)

    # Add horizontal line at the average quarterly revenue
    plt.axhline(avg_quarterly_revenue, linestyle='--', color='orange',linewidth=2, label='Q2 Average Revenue')

    ax.set_title('Amazon India Net Revenue', fontsize=20, x=.19, y=1.05)
    ax.text(-.08, 1.02, 'Q2 FY22', fontsize=15, color='#878787', transform=ax.transAxes)
    ax.set_xlabel(None)
    ax.set_yticklabels(list(range(0,41,5)))
    ax.set_ylabel('Net Revenue in 10,000 dollars', fontsize=12, labelpad=3)

    ax.yaxis.grid(linestyle='--', color='gray', linewidth=0.5, dashes=(8, 5))
    ax.xaxis.grid(False)


    plt.legend(bbox_to_anchor=(1,1.05), fontsize=12, fancybox=True)

    ax.tick_params(axis='both', labelsize=12)
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')

    # Display the plot using Streamlit
    st.pyplot(fig)

def plot_average_order_amount(data):
    # Group the data by month and calculate the average order value
    monthly_aov = data.groupby(pd.Grouper(key='date', freq='M')).agg({'order_amount_($)': 'sum', 'order_ID': 'nunique'})
    monthly_aov['average_order_value'] = monthly_aov['order_amount_($)'] / monthly_aov['order_ID']

    # Calculate percent change from previous month
    monthly_aov['pct_change'] = monthly_aov['average_order_value'].pct_change() * 100

    # Create a barplot of the average order value per month
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(x=monthly_aov.index.strftime('%b'), y=monthly_aov['average_order_value'], ax=ax, color='#878787')

    # Add line plot of the average order value per month
    ax.plot(monthly_aov.index.strftime('%b'), monthly_aov['average_order_value'], linestyle='--', linewidth=2, color='orange', marker='o')

    # Add callout for percent increase from April to June
    apr_val = monthly_aov['average_order_value'][0]
    jun_val = monthly_aov['average_order_value'][2]
    pct_change = ((jun_val - apr_val) / apr_val) * 100
    ax.annotate(f'Increase of {pct_change:.2f}% from Apr to Jun',fontweight='bold', xy=(2,8.074941567466606), xytext=(1.65, 8.264941567466606), fontsize=13, ha='center', va='bottom', arrowprops=dict(arrowstyle='->', color='black', lw=1.5, connectionstyle="arc3,rad=-0.1"))

    # Set labels and title
    ax.set_title('Average Monthly Order Amount', fontsize=20, x=.22, y=1.07)
    ax.text(-0.09, 1.04, 'Q2 FY22', fontsize=15, color='#878787', transform=ax.transAxes)
    ax.set_xlabel(None)
    ax.set_ylabel('Average Order Value ($)', fontsize=12, labelpad=3)
    ax.set_ylim(7.20, 8.50)
    ax.yaxis.grid(linestyle='--', color='gray', linewidth=0.5, dashes=(8, 5))

    ax.tick_params(axis='both', labelsize=12)
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')

    # Display the plot using Streamlit
    st.pyplot(fig)

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
    
    # Add more conditions as needed

def plot_top_product_revenue(data):
    fig, ax = plt.subplots(figsize=(8,6))

    # Define the desired order of months
    month_order = ['April', 'May', 'June']

    # Filter the data to only include the four product categories of interest
    sales_data = data[data['product_category'].isin(['Western Dress', 'Top', 'kurta', 'Set'])]

    # Convert the date column to a datetime object
    sales_data['date'] = pd.to_datetime(sales_data['date'])

    # Extract the month from the date column and set it as a new column
    sales_data['month'] = sales_data['date'].dt.month_name()

    # Aggregate the sales data by month and product category
    sales_by_month = sales_data.groupby(['month', 'product_category'])['order_amount_($)'].sum().reset_index()

    # Convert the month column to a categorical data type with the desired order
    sales_by_month['month'] = pd.Categorical(sales_by_month['month'], categories=month_order, ordered=True)

    # Plot the sales data using seaborn
    ax = sns.barplot(x='month', y='order_amount_($)', hue='product_category', data=sales_by_month,
                     palette=['#969696', '#bdbdbd', 'orange', '#d9d9d9'])

    # Extract the sales data for Western Dress
    sales_wd = sales_by_month[sales_by_month['product_category'] == 'Western Dress'].reset_index(drop=True)
    sales_wd['month'] = pd.Categorical(sales_wd['month'], categories=month_order, ordered=True)
    sales_wd.sort_values(by='month',inplace=True)
    # Add line plot for total monthly revenue of Western Dress
    ax.plot([0.1,1.1,2.1], sales_wd['order_amount_($)'], color='black', linestyle='--', linewidth=2, marker='o')


    # Add annotation for percent increase from April to June for Western Dress
    pct_increase = (sales_wd.loc[1, 'order_amount_($)'] - sales_wd.loc[0, 'order_amount_($)']) / sales_wd.loc[0, 'order_amount_($)'] * 100
    ax.annotate(f'{pct_increase:.0f}% increase\n April to June',fontweight='bold', xy=(2.1, sales_wd.loc[2, 'order_amount_($)']), xytext=(1.88, sales_wd.loc[2, 'order_amount_($)'] + 40000),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5, connectionstyle="arc3,rad=0.1"))


    # Set the number of y ticks you want
    num_y_ticks = 10

    # Calculate the y tick values
    y_tick_values = np.linspace(ax.get_yticks()[0], ax.get_yticks()[-1], num_y_ticks)

    # Set the y ticks
    ax.set_yticks(y_tick_values)


    # Add title and axis labels
    ax.set_title('Top Product Revenue by Month', fontsize=20, x=.22, y=1.07)
    ax.text(-0.09, 1.04, 'Q2 FY22', fontsize=15, color='#878787', transform=ax.transAxes)

    plt.legend(bbox_to_anchor=(1,1), fontsize=12, framealpha=1)

    ax.set_xlabel(None)
    ax.set_ylabel('Net Revenue in 10,000 dollars', fontsize=12, labelpad=3)
    ax.set_yticklabels(list(range(0,46,5)))
    ax.yaxis.grid(linestyle='--', color='gray', linewidth=0.5, dashes=(8, 5))

    ax.tick_params(axis='both', labelsize=12)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')

    # Display the plot using Streamlit
    st.pyplot(fig)

def plot_percent_product_revenue(data):
    # Group the data by product category and calculate the total sales
    sales_by_category = data.groupby('product_category')['order_amount_($)'].sum()

    # Filter the categories to include
    included_categories = ['Set', 'kurta', 'Western Dress', 'Top', 'Ethnic Dress', 'Blouse']
    sales_by_category = sales_by_category.loc[included_categories]

    # Calculate the total revenue
    total_revenue = sales_by_category.sum()

    # Calculate the percentage of total revenue for each category
    sales_by_category_pct = (sales_by_category / total_revenue) * 100

    # Sort the categories by total sales
    sales_by_category_pct = sales_by_category_pct.sort_values(ascending=False)

    # Create a bar chart to show the sales by product category
    fig, ax = plt.subplots(figsize=(12,8))
    palette_colors = ['orange' if cat in ['Set', 'Western Dress'] else '#878787' for cat in sales_by_category_pct.index]
    sns.barplot(x=sales_by_category_pct.index, y=sales_by_category_pct.values, ax=ax, palette=palette_colors)

    # Set font sizes for x and y labels, title, and ticks
    ax.set_ylabel('Percentage of Total Revenue', labelpad=1)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Product Category', labelpad=5)
    ax.set_title('Percentage of Product Category for Net Revenue', fontsize=20, x=0.255, y=1.05, pad=10)
    ax.text(-.07, 1.04, 'Average Cost per Product Displayed', fontsize=15, color='#878787', transform=ax.transAxes)
    ax.tick_params(axis='both', labelsize=12)
    ax.yaxis.grid(linestyle='--', color='gray', linewidth=0.5, dashes=(8, 5))
    ax.xaxis.grid(False)

    # Set font sizes for the bars and add annotations for Set, kurta, and Western Dress
    for i, category in enumerate(sales_by_category_pct.index):
        avg_cost = data[data['product_category'] == category]['order_amount_($)'].mean()
        if category in ['Set', 'Western Dress']:
            ax.text(i, sales_by_category_pct.values[i] +.1, f'${avg_cost:.2f}', ha='center', fontsize=18, fontweight='bold')
        else:
            ax.text(i, sales_by_category_pct.values[i] +.1, f'${avg_cost:.2f}', ha='center', fontsize=13)

    # Add a callout to emphasize the importance of western dresses for diversifying revenue
    western_sales = sales_by_category_pct['Western Dress']
    western_index = sales_by_category_pct.index.get_loc('Western Dress')

    # Define the callout box properties
    bbox_props = dict(boxstyle='round', facecolor='white', edgecolor='black', alpha=1)
    arrow_props = dict(facecolor='black', arrowstyle='wedge', alpha=0.5)

    # Set the position of the callout box
    x_pos = western_index
    y_pos = western_sales + 2
    x_text = x_pos + 0.5
    y_text = y_pos - 8

    # Calculate the percentage of revenue from western dresses
    western_pct = (western_sales / total_revenue) * 100

    # Add the callout box to the plot
    ax.annotate('With their high price point and strong sales performance,\nwestern dresses are a key driver of our revenue.\nBy prioritizing the sale of these products,\nwe can build a more resilient and diversified business.', xy=(x_pos, y_pos+2), xytext=(x_text+1, y_text+35), fontsize=14,
    arrowprops=arrow_props, bbox=bbox_props, ha='center', va='center')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')

    # Display the plot using Streamlit
    st.pyplot(fig)

def plot_sales_by_product_size(data):
    # Group the data by product size and calculate the total sales
    sales_by_size = data.groupby('size')['order_amount_($)'].sum()

    # Create a horizontal bar chart to show the sales by product size
    fig, ax = plt.subplots(figsize=(12,6))

    # Use a color palette to highlight specific sizes
    palette_colors = ['orange' if size in ['S', 'M', 'L'] else '#878787' for size in sales_by_size.index]
    sns.barplot(x=sales_by_size.index, y=sales_by_size.values, ax=ax, palette=palette_colors)

    # Set font sizes for x and y labels, title, and ticks
    ax.set_xlabel('Product Size', labelpad=3, fontsize=14)
    ax.set_ylabel('Net Revenue in 10,000 dollars', labelpad=3, fontsize=14)
    ax.set_yticklabels(list(range(0,20,2)))
    ax.set_title('Sales by Product Size', fontsize=20, x=0.085, y=1.05, pad=10)
    ax.text(-0.06, 1.04, 'Q2 FY22', fontsize=15, color='#878787', transform=ax.transAxes)
    ax.tick_params(axis='both', labelsize=12)
    ax.yaxis.grid(linestyle='--', color='gray', linewidth=0.5, dashes=(8, 5))
    ax.xaxis.grid(False)

    # Set the number of y ticks you want
    num_y_ticks = 10
    # Calculate the y tick values
    y_tick_values = np.linspace(ax.get_yticks()[0], ax.get_yticks()[-1], num_y_ticks)
    # Set the y ticks
    ax.set_yticks(y_tick_values)

    # Set font sizes for the bars and add annotations for S, M, and L sizes
    for i, size in enumerate(sales_by_size.index):
        if size in ['S', 'M', 'L']:
            ax.text(i, sales_by_size.values[i], f'{sales_by_size.values[i]/10000:.0f}k', ha='center', fontsize=14, fontweight='bold', color='black')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')

    # Display the plot using Streamlit
    st.pyplot(fig)

def plot_sales_by_quartile(data):
    # Define the color palette for the product categories
    colors = {'Top': '#d9d9d9', 'Set': '#969696', 'kurta': '#bdbdbd', 'Western Dress':'orange'}

    # Group the data by state and calculate the total sales
    sales_by_state = data.groupby('state')['order_amount_($)'].sum()

    # Get the top 5 and bottom 5 states by sales
    n_states = len(sales_by_state)
    quartiles = pd.qcut(sales_by_state, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
    top_states = []
    for q in ['Q1', 'Q2', 'Q3', 'Q4']:
        top_states += sales_by_state[quartiles == q].nlargest(5).index.tolist()

    # Filter the dataframe to include only the top states
    top_sales = data[data['state'].isin(top_states)]

    # Group the data by state and product, and calculate the total sales
    sales_by_state_product = top_sales.groupby(['state', 'product_category'])['order_amount_($)'].sum().reset_index()

    # Get the top 3 products for each quartile
    top_products = []
    for q in ['Q1', 'Q2', 'Q3', 'Q4']:
        top_products += sales_by_state_product[sales_by_state_product['state'].isin(sales_by_state[quartiles == q].index)].groupby('state').apply(lambda x: x.nlargest(3, 'order_amount_($)'))['product_category'].tolist()

    # Create a figure with four subplots
    fig, axs = plt.subplots(2, 2, figsize=(16, 12), sharey=False)

    # Create the subplot for quartile 1
    q1_sales = sales_by_state_product[sales_by_state_product['state'].isin(sales_by_state[quartiles == 'Q1'].index)]
    q1_sales = q1_sales[q1_sales['product_category'].isin(top_products)]
    sns.barplot(x='state', y='order_amount_($)', hue='product_category', data=q1_sales, ax=axs[0, 0], palette=colors)
    axs[0, 0].legend().set_visible(False)
    axs[0, 0].set_title('Sales by Q1 States (lowest revenue quartile)')
    axs[0, 0].set_xlabel('State')
    axs[0, 0].set_ylabel('Total Sales ($)')

    # Create the subplot for quartile 2
    q2_sales = sales_by_state_product[sales_by_state_product['state'].isin(sales_by_state[quartiles == 'Q2'].index)]
    q2_sales = q2_sales[q2_sales['product_category'].isin(top_products)]
    sns.barplot(x='state', y='order_amount_($)', hue='product_category', data=q2_sales, palette=colors, ax=axs[0, 1])
    axs[0, 1].legend().set_visible(False)
    axs[0, 1].set_title('Sales by Q2 States (second-lowest revenue quartile)')
    axs[0, 1].set_xlabel('State')
    axs[0, 1].set_ylabel('Total Sales ($)')

    # Create the subplot for quartile 3
    q3_sales = sales_by_state_product[sales_by_state_product['state'].isin(sales_by_state[quartiles == 'Q3'].index)]
    q3_sales = q3_sales[q3_sales['product_category'].isin(top_products)]
    sns.barplot(x='state', y='order_amount_($)', hue='product_category', data=q3_sales, palette=colors, ax=axs[1, 0])
    axs[1, 0].legend().set_visible(False)
    axs[1, 0].set_title('Sales by Q3 States (second-highest revenue quartile)')
    axs[1, 0].set_xlabel('State')
    axs[1, 0].set_ylabel('Total Sales ($)')

    # Create the subplot for quartile 4
    q4_sales = sales_by_state_product[sales_by_state_product['state'].isin(sales_by_state[quartiles == 'Q4'].index)]
    q4_sales = q4_sales[q4_sales['product_category'].isin(top_products)]
    sns.barplot(x='state', y='order_amount_($)', hue='product_category', data=q4_sales, palette=colors, ax=axs[1, 1])
    axs[1, 1].legend().set_visible(False)
    axs[1, 1].set_title('Sales by Q4 States (highest revenue quartile)')
    axs[1, 1].set_xlabel('State')
    axs[1, 1].set_ylabel('Total Sales ($)')

    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=.9, wspace=.21, bottom=.2)

    # Rotate the x-axis tick labels
    for ax in axs.flat:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    # Add a single legend to the figure
    handles, labels = axs[1, 1].get_legend_handles_labels()
    fig.legend(handles, labels, loc='center', ncol=len(labels), title='Product Category', fontsize=15, title_fontsize = 15)

    plt.suptitle("Identifying Top 4 Products for Top 5 States in each Revenue Quartile", fontsize = 25)
    # Show the figure
    st.pyplot(fig)
