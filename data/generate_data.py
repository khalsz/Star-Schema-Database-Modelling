import pandas as pd
from faker import Faker
import datetime
from datetime import datetime as dt
import numpy as np
import random

fake = Faker('en_US')


def fake_product_data(): 
    name = fake.word()
    category = fake.word(ext_word_list=["agriculture", "telecoms", "food"])
    
    product = {
        'product id': fake.random_number(digits=5), 
        'name': name, 
        'category':category, 
        'price': random.randrange(1000,5000, 500), 
        'description':str.lower(f"this name of product is {name} and catgeory {category}")  
    }
    return product

def fake_customer_data(date): 
    customer = {
        'customer id': fake.random_number(digits=5),
        'name': fake.first_name(),
        "location": fake.country(),
        'email': fake.email(),
        'registration date': date
    }
    return customer
def fake_time_data(date): 
    times = {
        'order time': date, 
        'order month': date.month,
        'order year': date.year
    }
    return times
    
def fake_fact_data(customer_data, product_data, date): 

    fact = {
        'order id': fake.random_number(digits=5),
        'customer id': customer_data['customer id'], 
        'product id': product_data['product id'],
        'order date': date, 
        'quantity': fake.random_number(digits=2), 
        'amount': fake.random_number(digits=3)
    }
    return fact


def generate_tables(records): 
    fact_table = []
    time_table = []
    product_table = []
    customer_table = []
    for i in range(records): 
        date = dt.strptime(fake.date(pattern="%Y-%m-%d", 
                            end_datetime=datetime.date(2024, 4,1)), 
                           "%Y-%m-%d").date()
        product = fake_product_data()
        customer = fake_customer_data(date)
        times = fake_time_data(date=date)
        fact = fake_fact_data(customer, product, date)
        product_table.append(product)
        time_table.append(times)
        fact_table.append(fact)
        customer_table.append(customer)
        
    df_fact = pd.DataFrame.from_dict(fact_table)
    df_product = pd.DataFrame.from_dict(product_table)
    df_customer = pd.DataFrame.from_dict(customer_table)
    df_time = pd.DataFrame.from_dict(time_table)

    return df_fact, df_product, df_customer, df_time

if __name__ == '__main__': 
    generate_tables(20)