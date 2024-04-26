from database.db_connect import db_connection
from database.db_query import query_table, add_foreign_key, add_primary_key
from data.generate_data import generate_tables
from config.config import dbconfig
from database.create_table import create_db_table


def main(num_records): 
    """
    Main function to generate data tables, create database tables, add primary and foreign keys, and execute queries.

    Args:
        num_records (int): Number of records to generate for each table.

    """
    try:
        # Generate data tables
        df_fact, df_product, df_customer, df_time = generate_tables(records=num_records)
        
        # Establish database connection
        connection, engine = db_connection(dbconfig['USERNAME'], dbconfig['PASSWORD'], 
                    dbconfig['HOST'], 'online_retail')
        
        # Create database tables
        create_db_table(df_fact, engine, 'fact_table')
        create_db_table(df_product, engine, 'product_table')
        create_db_table(df_customer, engine, 'customer_table')
        create_db_table(df_time, engine, 'time_table')
        
        # Add primary keys
        add_primary_key('fact_table', 'order id', connection)
        add_primary_key('product_table', 'product id', connection)
        add_primary_key('customer_table', 'customer id', connection)
        add_primary_key('time_table', 'order time', connection)

        # Add foreign keys
        add_foreign_key('fact_table', 'product_fk', 'product id', 'product_table', 'product id', connection)
        add_foreign_key('fact_table', 'customer_fk', 'customer id', 'customer_table', 'customer id', connection)
        add_foreign_key('fact_table', 'date_fk', 'order date', 'time_table', 'order time', connection)
        
        # Execute query statement list
        query_statements = [ "select p.name, sum(f.quantity) as total_quanity  from fact_table f inner join product_table p \
                        on f.\"product id\"=p.\"product id\" where extract(year from f.\"order date\") < 2020 group by p.name" , 
                           "select avg(amount) as avg_amount from fact_table group by extract(month from \"order date\")", 
                           "select c.location,  sum(f.quantity) as total_quanity from fact_table f inner join customer_table c \
                               on f.\"customer id\"=c.\"customer id\" group by c.location", 
                            "select p.name, max(f.amount) as max_revenue from fact_table f inner join product_table p \
                                on f.\"product id\"=p.\"product id\" group by p.name"]

        for statement in query_statements: 
            query_result = query_table(statement, connection)
            print(query_result)
            
    except Exception as e: 
        raise Exception(f"Error: {e}")

if __name__ == "__main__": 
    main(20)
        
