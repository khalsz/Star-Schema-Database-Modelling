from sqlalchemy import text

def create_db_table(df, engine, table_name): 
    """
    Creates a database table from a DataFrame.

    Args:
        df (DataFrame): The DataFrame containing the data to be stored in the database.
        engine (Engine): SQLAlchemy engine object for the database.
        table_name (str): Name of the table to be created.

    Raises:
        Exception: If an error occurs during the table creation process.
    """
    try: 
        # Create the table in the database from the DataFrame
        df.to_sql(table_name, con=engine, if_exists="replace", index_label='id', index=False)
        print("successfuly created table")
    except Exception as e: 
        # Raise an exception if an error occurs
        raise(f"Error creating table: {e}")
    