from sqlalchemy import create_engine, text
import pandas as pd


def query_table(query_statement, connection): 
    """
    Execute a SQL query statement and return the result as a DataFrame.

    Args:
        query_statement (str): SQL query statement to execute.
        connection (Connection): SQLAlchemy connection object.

    Returns:
        DataFrame: DataFrame containing the query result.

    Raises:
        Exception: If an error occurs during the query execution.
    """
    try: 
        # Execute the SQL query statement
        result = connection.execute(text(query_statement))
        
        # Fetch all rows and column names from the query result
        df_table = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df_table
    except Exception as e: 
        # Raise an exception if an error occurs
        raise Exception(f"Error querying table: {e}")
        

def add_primary_key(table_name, column, connection):
    """
    Adds a primary key constraint to a table in the database.

    Args:
        table_name (str): Name of the table.
        column (str): Name of the column to be set as the primary key.
        connection (Connection): SQLAlchemy connection object.

    Raises:
        Exception: If an error occurs while adding the primary key.
    """
    try: 
        # Execute SQL statement to add primary key
        connection.execute(text(f"alter table \"{table_name}\" add primary key(\"{column}\")"))
        print(f"added primary key: '{column}' to table: {table_name} successfully")
    except Exception as e: 
        # Raise an exception if an error occurs
        raise Exception(f"Error: {e}") 

def add_foreign_key(target_table, foreign_key, target_column, ref_table, ref_column, connection): 
    """
    Adds a foreign key constraint to a table in the database.

    Args:
        target_table (str): Name of the table to add the foreign key constraint to.
        foreign_key (str): Name of the foreign key constraint.
        target_column (str): Name of the column in the target table.
        ref_table (str): Name of the referenced table.
        ref_column (str): Name of the referenced column.
        connection (Connection): SQLAlchemy connection object.

    Raises:
        Exception: If an error occurs while adding the foreign key.
    """
    try: 
        # Execute SQL statement to add foreign key
        connection.execute(text(f"alter table \"{target_table}\" add constraint {foreign_key} " \
            f"foreign key(\"{target_column}\") references \"{ref_table}\"(\"{ref_column}\")"))
        print(f"added foreign key: '{foreign_key}' to table: {target_table} successfully")
    except Exception as e: 
        # Raise an exception if an error occurs
        raise Exception(f"Error: {e}")