# Star Schema Database Modeller
## Overview
The Star Schema Database Modeller is a Python project designed to automate the process of generating synthetic data, creating a star schema database model, and executing predefined queries. The project utilizes SQLAlchemy for database interaction and Faker for generating synthetic data.

## Features
- Generate synthetic data tables for fact and dimension tables.
- Create database tables in PostgreSQL.
- Add primary and foreign key constraints to database tables.
- Execute predefined queries on the database.

## Project Structure
- database/: Package containing modules for database interaction.
    - db_connect.py: Module to establish connections to a PostgreSQL database.
    - db_query.py: Module to execute SQL queries and add primary/foreign keys.
    - create_table.py: Module to create database tables from DataFrames.
- data/: Package containing modules for generating synthetic data.
    - generate_data.py: Module to generate synthetic data for fact and dimension tables.
- config/: Package containing configuration files.
    - config.py: Configuration file for database connection parameters.
- README.md: Readme file providing an overview of the project.

## Usage
1. Install the required Python packages listed in the requirements.txt file.
2. Configure the database connection parameters in the config.py file.
3. Run the main.py script to generate synthetic data, create database tables, add primary/foreign keys, and execute queries.
4. Check the console output for status messages and query results.
5. Verify the data in the PostgreSQL database.

## Configuration
- Database Connection: Set up the PostgreSQL connection parameters (username, password, host, database name) in the config.py file.
- Query Statements: Define the SQL query statements in the main.py script.

## Dependencies
- Python 3.x
- SQLAlchemy
- Faker
- Pandas

## Contribution
Contributions are welcome! Here's how you can contribute:

 1. Fork the repository.
 2. Create a new branch (git checkout -b feature).
 3. Make changes and commit them (git commit -am 'Add new features').
 4. Push to the branch (git push origin feature).
 5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE.txt file for details.