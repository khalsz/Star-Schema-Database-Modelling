from sqlalchemy import create_engine, text
import pyodbc
from sqlalchemy_utils import database_exists, create_database

def db_connection(username, password, host, db_name): 
    try: 
        conn_str = f'postgresql+psycopg2://{username}:{password}@{host}:5432/{db_name}' 
        engine = create_engine(conn_str, echo=True, isolation_level = "AUTOCOMMIT")
        
        if not database_exists(engine.url): 
            create_database(engine.url)
        
        connection = engine.connect()
        return connection
    except Exception as e: 
        raise Exception (f"Error: {e}")

