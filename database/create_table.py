from sqlalchemy import insert, Column, Integer, ForeignKey, String,  TIMESTAMP, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, backref

Base = declarative_base()


class Product(Base): 
    __tablename__ = "product_dimension"
    product_id = Column('product_id', Integer, primary_key=True)
    name = Column('name', String(40))
    category = Column('category', String(40))
    price = Column('price', Integer)
    description = Column('description', String(100))
    

class Time(Base): 
    __tablename__ = "time_dimension"
    time_id = Column('time_id', Integer, primary_key=True)
    order_time = Column('order_time', TIMESTAMP)
    order_month = Column('order_month', Integer)
    order_year = Column('order_year', Integer)
    
class Customer(Base): 
    __tablename__ = "customer_dimension"
    customer_id = Column('customer_id', Integer, primary_key=True)
    name = Column('name', String(40))
    email = Column('email', String(65))
    location = Column('location', String(50))
    registration_date = Column('registration_date', DATE)

class Order(Base): 
    __tablename__ = 'order_dimension'
    order_id = Column('order_id', Integer, primary_key=True)
    order_type = Column('order_type', String(40))    
    
class Fact(Base): 
    __tablename__ = "order_fact_table"
    id = Column('id', Integer, primary_key=True)
    order_date = Column('order_date', DATE )
    quantity = Column('quantity', Integer)
    amount = Column('amount', Integer)
    product_id = Column('product_id', Integer, ForeignKey("product_dimension.product_id"), nullable=False)
    product = relationship("Product")
    time_id = Column('time_id', Integer, ForeignKey(Time.time_id), nullable=False)
    time = relationship('Time', backref=backref('Fact'))
    customer_id = Column('customer_id', Integer, ForeignKey("customer_dimension.customer_id"), nullable=False)
    customer = relationship('Customer')
    order_id = Column('order_id', Integer, ForeignKey("order_dimension.order_id"), nullable=False)
    order = relationship('Order')

def create_db_table(engine): 
    """
    Creates database tables based on SQLAlchemy metadata.

    This function drops existing tables (if any) and creates new tables based on the SQLAlchemy metadata defined in Base.

    Args:
        engine (Engine): SQLAlchemy engine object for the database.

    Raises:
        Exception: If an error occurs during the table creation process.
    """
    try: 
        # Drop existing tables
        Base.metadata.drop_all(engine, 
                               tables=[Base.metadata.tables["order_dimension"], 
                                       Base.metadata.tables["customer_dimension"], 
                                       Base.metadata.tables["product_dimension"], 
                                       Base.metadata.tables["time_dimension"], 
                                       Base.metadata.tables["order_fact_table"]])
        # Create new tables
        Base.metadata.create_all(engine)
        print("all table successfully created")
        
    except Exception as e: 
        raise Exception(f"Error creating tables: {e}")
        
def populate_tables(engine, fact_dicts, product_dicts, customer_dicts, time_dicts, order_dicts): 
    """
    Populates database tables with data.

    Args:
        engine (Engine): SQLAlchemy engine object for the database.
        fact_dicts (list of dict): List of dictionaries containing data for the Fact table.
        product_dicts (list of dict): List of dictionaries containing data for the Product table.
        customer_dicts (list of dict): List of dictionaries containing data for the Customer table.
        time_dicts (list of dict): List of dictionaries containing data for the Time table.
        order_dicts (list of dict): List of dictionaries containing data for the Order table.

    Raises:
        Exception: If an error occurs during the data insertion process.
    """
    try: 
        with Session(engine) as session: 
            # Insert data into Product table
            session.execute(insert(Product), product_dicts)
            # Insert data into Time table
            session.execute(insert(Time), time_dicts)
            # Insert data into Customer table
            session.execute(insert(Customer), customer_dicts)
            # Insert data into Order table
            session.execute(insert(Order), order_dicts)
            # Insert data into Fact table
            session.execute(insert(Fact), fact_dicts)
            session.commit()
    except Exception as e: 
        raise Exception("Error populating table with data: {e}")
