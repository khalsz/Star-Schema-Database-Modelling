import pandas as pd
from faker import Faker
import datetime
from datetime import datetime as dt
import random

fake = Faker('en_US')


def fake_product_data(): 
    name = fake.word()
    category = fake.word(ext_word_list=["agriculture", "telecoms", "food"])
    
    product = {
        'product_id': fake.random_number(digits=5), 
        'name': name, 
        'category':category, 
        'price': random.randrange(1000,5000, 500), 
        'description':str.lower(f"this name of product is {name} and catgeory {category}")  
    }
    return product

def fake_customer_data(date): 
    customer = {
        'customer_id': fake.random_number(digits=5),
        'name': fake.first_name(),
        "location": fake.country(),
        'email': fake.email(),
        'registration_date': date
    }
    return customer
def fake_time_data(date, sn): 
    times = {
        'time_id': sn,
        'order_time': date, 
        'order_month': date.month,
        'order_year': date.year
    }
    return times
    
def fake_fact_data(customer_data, product_data, date, order, time): 

    fact = {
        'order_id': order['order_id'],
        'customer_id': customer_data['customer_id'], 
        'product_id': product_data['product_id'],
        'time_id': time['time_id'],
        'order_date': date, 
        'quantity': fake.random_number(digits=3), 
        'amount': fake.random_number(digits=3)
    }
    return fact

def fake_order_data(): 
    types = fake.word(ext_word_list=["E-commerce", "retail", "healthcare"])
    
    order = {
        'order_id': fake.random_number(digits=5), 
        'order_type': types, 
    }
    return order

def generate_tables(records): 
    """
    Generate synthetic data tables.

    Args:
        records (int): Number of records to generate for each table.

    Returns:
        tuple: A tuple containing list of dictionaries for the fact, product, customer, order, and time tables.

    """
    fact_dicts = []
    time_dicts = []
    product_dicts = []
    customer_dicts = []
    order_dicts = []
    
    # Generate data for the specified number of records
    for i in range(records): 
        # Generate a random date within the specified range
        date = dt.strptime(fake.date(pattern="%Y-%m-%d", 
                            end_datetime=datetime.date(2024, 4,1)), 
                           "%Y-%m-%d").date()
        # Generate data for each table
        product = fake_product_data()
        customer = fake_customer_data(date)
        order = fake_order_data()
        times = fake_time_data(date=date, sn=i)
        fact = fake_fact_data(customer, product, date, order, times)
        
        # append data record to list
        product_dicts.append(product)
        time_dicts.append(times)
        fact_dicts.append(fact)
        customer_dicts.append(customer)
        order_dicts.append(order)

    return fact_dicts, product_dicts, customer_dicts, time_dicts, order_dicts
