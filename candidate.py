"""
Step 1
Clone Public Repository: 
`https://github.com/bilalbobat/data_engineer`

Step 2
Navigate into the Directory data_engineer: 

Step 3
Create a Virtual Environment

Step 4
Activate the Virtual Environment

Step 5
Install Dependencies from requirements.txt file 

Instructions:

Populate `candidate.py` with the relevant code by completing each of the `query_str`
with missing code.

Run `candidate.py`
"""

# Q1.a
"""
Question: How can I implement a logging mechanism in a Python application to log SQL queries, including the setup for a log file named 'app.log', 
configuring the logging level to 'INFO', specifying a custom format for log messages '%(asctime)s - %(levelname)s - %(message)s', and ensuring 
that the log file is overwritten each time the application runs? 
"""

# Q1.b
"""
Question: How can I create a function to log both the question and the corresponding SQL query?
"""

from jinja2 import Template

# Example
table_schema  = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    user_age INT,
    user_email VARCHAR(100)
);
"""
question = "Question: What is the SQL query to select all columns from a table named 'users'?"

query_str = "SELECT * FROM users"

template = Template(query_str)
query = template.render()
log_query(question, query)

# Q2
table_schema  = """
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    product_category VARCHAR(50),
    sales_amount DECIMAL(10, 2),
    employee_id INT
);
"""
question = """Question: Write a SQL query to calculate the 'running total' of 'sales_amount' for each 'product_category' 
ensuring that the results are ordered by 'sale_date'? Return the 'product_category', 'sales_amount', and 'running_total' in the output.
"""

query_str = """
"""

template = Template(query_str)
query = template.render()
log_query(question, query)

# Q3
table_schema  = """
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    product_category VARCHAR(50),
    sales_amount DECIMAL(10, 2),
    employee_id INT
);
"""
question = """Question: Write a SQL query to retrieve the top 2 'sales_amounts' for each 'employee_id' from the 'sales' table. 
Ensure that the results include the 'employee_id', 'sales_amount', and a ranking of the sales amounts. 
The output should be ordered by 'employee_id' and 'sales_amount' in descending order."""

query_str = """
"""

template = Template(query_str)
query = template.render()
log_query(question, query)

# Example
table_schema  = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    user_age INT,
    user_email VARCHAR(100)
);
"""
question = "Question: What is the SQL query to select all columns from a table named 'users'?"
query_str = "SELECT * FROM {{ table_name }}"
template = Template(query_str)
query = template.render(table_name="users")
log_query(question, query)

# Q4
table_schema  = """
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    order_date DATE
);
"""
question = "What is the SQL query to select all columns from 'orders' where 'product' is 'Laptop' and 'quantity' is greater than or equal to 5?"
query_str = ""
template = Template(query_str)
query = template.render(product='Laptop', min_quantity=5)
log_query(question, query)

# Q5
table_schema  = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    user_age INT,
    user_email VARCHAR(100)
);
"""

question = "What is the SQL query to select all users and conditionally filter by 'user_age' only if 'user_age' is 18 or older?"
query_str = """"""
template = Template(query_str)
query = template.render(user_age=18)
log_query(question, query)

# Q6
table_schema  = """
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    order_date DATE
);
"""
question = "What is the SQL query to select 'orders' where 'order_id' is in a given list?"
query_str = """"""
template = Template(query_str)
query = template.render(order_ids=[1234, 5678, 9012])
log_query(question, query)