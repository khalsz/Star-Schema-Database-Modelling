from database.db_connect import db_connection
from database.db_query import query_table
from data.generate_data import generate_tables
from config.config import dbconfig
from database.create_table import create_db_table, populate_tables


def main(num_records): 
    """
    Main function to generate data tables, create database tables, add primary and foreign keys, and execute queries.

    Args:
        num_records (int): Number of records to generate for each table.

    """
    try:
        # Generate data tables
        fact_dicts, product_dicts, customer_dicts, time_dicts, order_dicts = generate_tables(records=num_records)
        
        
        # Establish database connection
        connection, engine = db_connection(dbconfig['USERNAME'], dbconfig['PASSWORD'], 
                    dbconfig['HOST'], 'online_retail')
        
        # Create database tables
        create_db_table(engine)
        
        populate_tables(engine,  fact_dicts, product_dicts, customer_dicts, time_dicts, order_dicts)
        
        # Execute query statement list
        query_statements = [ "select p.name, sum(f.quantity) as total_quanity  from order_fact_table f inner join product_dimension p \
                        on f.product_id=p.product_id where extract(year from f.order_date) < 2020 group by p.name" , 
                           "select avg(amount) as avg_amount from order_fact_table group by extract(month from order_date)", 
                           "select c.location,  sum(f.quantity) as total_quanity from order_fact_table f inner join customer_dimension c \
                               on f.customer_id=c.customer_id group by c.location", 
                            "select p.name, max(f.amount) as max_revenue from order_fact_table f inner join product_dimension p \
                                on f.product_id=p.product_id group by p.name"]

        for statement in query_statements: 
            query_result = query_table(statement, connection)
            print(query_result)
            
    except Exception as e: 
        raise Exception(f"Error: {e}")

if __name__ == "__main__": 
    main(20)
        
