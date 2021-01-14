''' This file contains our groups answers to Part 2: Pandas Questions. 
The answers have been written as functions as much as we deemed possible, and the print statements have been commented out. 
Simply uncomment and run for each questions :) '''


# Importing Libraries
import pandas as pd
from pandas import read_csv
from scipy import stats
import numpy as np
import datetime

'''
Question 16: Import datasets from the Data folder from CSV.
'''

# Importing Customer Dataset
customer_df = pd.read_csv('https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/customer.csv')
# Importing Products Dataset
products_df = pd.read_csv('https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/products.csv')
# Importing Retangles Dataset
rectangles_df = pd.read_csv('https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/rectangles_old.csv')
# Importing Sales Dataset
sales_df = pd.read_csv('https://raw.githubusercontent.com/JunaidMB/python_competition/master/questions/sales.csv')

# print(customer_df)
# print(products_df)
# print(rectangles_df)
# print(sales_df)

'''
Question 17: How many unique products are sold?
'''

def num_unique_products():
    # returning the length of the unique values in p_id column
    return len(sales_df['p_id'].unique())

# print(sales_df)

'''
Question 18: List the unique products sold.
'''

def unique_products():
    # returning the names of the unique products
    unique_prod = sales_df['product'].unique()
    return unique_prod

# print('The unique products sold are:', unique_products())

'''
Question 19: List the quantity sold for each product and product id (No Multilevel indexing).
'''

def quantity_for_products():
    # returning quantity sold for each product and p_id
    quant = sales_df.groupby(['product', 'p_id']).qty.agg('sum')
    return quant

# print(quantity_for_products())

'''
Question 20: For each product, give the total Quantity sold and the revenue earned from the total sales (price x quantity)
'''

def total_quantity_revenue():
    # merging the product and sales DataFrames to make producrts_sales_df
    products_sales_df = pd.merge(products_df, sales_df, on='product')
    # creating a revenue column which is the multiple of price and quantity columns
    products_sales_df['revenue'] = products_sales_df['price']*products_sales_df['qty']
    # returning the total quantity sold and revenue
    quant_revenue = products_sales_df.groupby(['product']).agg({'qty': 'sum', 'revenue':'sum'})
    return quant_revenue

# print(total_quantity_revenue())

'''
Question 21: List of quantity sold against each product and against each store and sort by store and product.
'''

def qty_prod_store():
    # grouping to return quatity sold for each product and store
    qty_prod_store = sales_df.groupby(['product', 'store']).qty.agg('sum')
    # sorting values in asceneding order
    qty_prod_store.sort_values(by=['product', 'store'], ascending=[True, True])
    return qty_prod_store

# print(qty_prod_store())

'''
Question 22: List of quantity sold against each Store with total turnover of the store.
'''

def qty_turnover():
    # merging products and sales DataFrames
    products_sales_df = pd.merge(products_df, sales_df, on='product')
    # grouping to return quantity sold and turnover for each store
    qty_store_tover = products_sales_df.groupby(['store']).agg({'qty':'sum', 'price':'sum'}) # use revenue instead of price
    return qty_store_tover

# print(qty_turnover())

'''
Question 23: List the products which are not sold
'''

def products_not_sold():
    # merging sales and product DataFrames
    products_sales_df = pd.merge(sales_df, products_df, on='p_id', how='right')
    # assigning products not sold to variable not_sold_df
    not_sold_df = products_sales_df[products_sales_df['sale_id'].isnull()]
    # returning product column of the not_sold DafaFrame
    not_sold = not_sold_df['product_y']
    return not_sold

# print('The products which are not sold are: \n', products_not_sold())

'''
Question 24: List of customers who have not purchased any product.
'''

def no_purchase_customers():
    # merging sales and customer DataFrame
    sales_customer_df = pd.merge(sales_df, customer_df, on='c_id', how='right')
     # assigning sales not made to variable not_purchase_df
    no_purchase_df = sales_customer_df[sales_customer_df['sale_id'].isnull()]
    # returning customer column in no_purchase DataFrame
    customers = no_purchase_df['Customer']
    return customers

# print('List of customers who have not purchased any products: \n', no_purchase_customers())
'''
Question 25: Assign a 'birthday_this_year' column to the customer table where each customer has a birthday associated with them in the yyyy-mm-dd format.
'''

def birthday():
    start_date = '2020-01-01'
    # creating new column in customer_df filled with preset start_date
    customer_df['birthday_this_year'] = start_date
    # iterating through customer_df rows to update birhday column
    for index, row in customer_df.iterrows():
        # for all rows except the first
        if index != 0:
            # calculating the birthday
            calc = datetime.datetime.strptime(customer_df['birthday_this_year'][index - 1], "%Y-%m-%d") + datetime.timedelta(days=row["c_id"]-1)
            # updating birthday column with calcualted date
            customer_df['birthday_this_year'][index] = datetime.datetime.strftime(calc, "%Y-%m-%d")
    return customer_df
birthday()
# print(birthday())

'''
Question 26: Make a dataframe for the new customer
'''

# new customer details
new_customer = pd.DataFrame({'c_id': [10, 11, 12, 13], 'Customer': ['James', 'Bill', 'Susie', 'Emma'], 'birthday_this_year': ['2020-07-28', '2020-04-05', '2020-11-25', '2020-06-14']})
# concatonating new_customer DataFrame with initial customer DataFrame
customer_df = pd.concat([customer_df, new_customer], ignore_index=True)
# sorting based on c_id
customer_df.sort_values(by='c_id')
# print(customer_df)

'''
Question 27: Add an indicator column in the sales table called 'qty_multiple_2' where 1 indicates if the qty is a multiple of 2 and 0 otherwise.
'''

def multiple_of_2():
    # creating qty_multiple_2 column and prefillinh with 0
    sales_df['qty_multiple_2'] = 0
    # iterating through sales_df rows
    for index, row in sales_df.iterrows():
        # whether qty is a multiple of 2
        if sales_df['qty'][index] % 2 == 0:
            sales_df['qty_multiple_2'][index] = 1
        else: 
        # whether qty is not a multiple of 2
            sales_df['qty_multiple_2'][index] = 0
    return sales_df

# print(multiple_of_2())

'''
Question 28: Create a column called Age in the new customers table where each customer has ages [24, 29, 42, 35, 32, 28, 19, 38, 27, 29, 34, 25]
'''

# creating new column for customer ages
customer_df['Age'] = [24, 29, 42, 35, 32, 28, 19, 38, 27, 29, 34, 25]
# print(customer_df)
# print(sales_df)

'''
Question 29: Compute the date of birth for each customer.
'''

def date_of_birth():
    # getting todays date, converting birthday_this_year to datetime and assigning that series to BDTY
    today = datetime.datetime.today()
    BDTY = pd.to_datetime(customer_df['birthday_this_year'])
    # creating DOB column in customr_df and pre-filling it with birthday_this_year
    customer_df['DOB'] = pd.to_datetime(customer_df['birthday_this_year'])
    for index, row in customer_df.iterrows():
        # if customer birthday has passed
        if today > BDTY[index]:
            # calculating year of birth
            YOB = today.year - customer_df['Age'][index]
        # if customer birthday has not passed
        else:
            YOB = BDTY[index].year - customer_df['Age'][index] - 1
        # replacing the years in DOB column with the correct year of birth calculated
        customer_df['DOB'][index] = customer_df["DOB"][index].replace(YOB)
    return customer_df

date_of_birth()

# print(customer_df[['Customer', 'DOB']])

'''
Question 30: In the most recent customer table, assign a column which tells us which astrology star sign each customer is.
'''

def horoscope(day, month):
    # assigning zodiac signs for each date range
    if month == 'december':
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 'january':
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 'february':
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 'march':
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 'april':
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 'may':
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 'june':
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 'july':
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 'august':
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 'september':
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 'october':
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 'november':
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    return(astro_sign)

customer_df['DOB']= pd.to_datetime(customer_df['DOB'])
customer_df['star_sign'] = customer_df['DOB'].apply(lambda customer_df: horoscope(customer_df.day, customer_df.strftime("%B").lower()))

print(customer_df)

'''
Question 31: Consider the rectangles dataset, read it in, compute the area of each rectangle and save the file to CSV called 'rectangles_new'.
'''

rectangles_df['area'] = rectangles_df['height']*rectangles_df['width']
rectangles_df.to_csv('rectangles_new.csv')


'''

Joke of the Question:

What do you get when you cross a pirate with a data scientist? Answer: Someone who specializes in Rrrr

'''