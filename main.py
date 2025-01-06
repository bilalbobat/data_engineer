"""
Question: How can I implement a logging mechanism in a Python application to log SQL queries, including the setup for a log file named app.log, 
configuring the logging level to INFO, specifying a custom format for log messages '%(asctime)s - %(levelname)s - %(message)s', and ensuring 
that the log file is overwritten each time the application runs? 

Additionally, how can I create a function to log both the question and the corresponding SQL query?
"""

import logging

def log_query(question, query):
    logging.info(f"\n{question}\n{query}")


logging.basicConfig(
    filename='app.log',  # Specify the file name
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the format of log messages
    filemode='w'  # Set filemode to 'w' to overwrite the log file
)


from jinja2 import Template

question = "Question: What is the SQL query to select all columns from a table named 'users'?"
query_str = "SELECT * FROM users"
template = Template(query_str)
query = template.render(table_name="users")
log_query(question, query)

question = """Question: Write a SQL query to calculate the 'running total' of 'sales_amount' for each 'product_category' 
ensuring that the results are ordered by 'sale_date'? Return the 'product_category', 'sales_amount', and 'running_total' in the output.
"""
query_str = """SELECT 
    product_category,
    sales_amount,
    SUM(sales_amount) OVER (PARTITION BY product_category ORDER BY sale_date) AS running_total
FROM sales
"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = """Question: Write a SQL query to retrieve the top 2 'sales_amounts' for each 'employee_id' from the 'sales' table. 
Ensure that the results include the 'employee_id', 'sales_amount', and a ranking of the sales amounts. 
The output should be ordered by 'employee_id' and 'sales_amount' in descending order."""
query_str = """
WITH RankedSales AS (
    SELECT 
        employee_id,
        sales_amount,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY sales_amount DESC) AS sales_rank
    FROM sales
)
SELECT 
    employee_id,
    sales_amount,
    sales_rank
FROM RankedSales
WHERE sales_rank <= 2
ORDER BY employee_id, sales_amount DESC;
"""

question = "Question: What is the SQL query to select all columns from a table named 'users'?"
query_str = "SELECT * FROM {{ table_name }}"
template = Template(query_str)
query = template.render(table_name="users")
log_query(question, query)

question = "What is the SQL query to select all columns from orders where product is 'Laptop' and quantity is greater than or equal to 5?"
query_str = "SELECT * FROM orders WHERE product = '{{ product }}' AND quantity >= {{ min_quantity }}"
template = Template(query_str)
query = template.render(product='Laptop', min_quantity=5)
log_query(question, query)

question = "What is the SQL query to select all users and conditionally filter by age if user_age is 18 or older?"
query_str = """SELECT * FROM users {% if user_age >= 18 %} WHERE age >= {{ user_age }}{% endif -%};"""
template = Template(query_str)
query = template.render(user_age=18)
log_query(question, query)

question = "What is the SQL query to select all users and check if they are adults based on user_age?"
query_str = """SELECT * FROM users WHERE {% if user_age >= 18 %} adult = True {% else %} adult = False {% endif -%};"""
template = Template(query_str)
query = template.render(user_age=30)
log_query(question, query)

question = "What is the SQL query to select products based on stock performance categories?"
query_str = """SELECT * FROM products where
{% if product_stock >= 1000 %} performance = 'bad' 
{% elif product_stock >= 300 and product_stock < 1000 %} performance = 'average' 
{% else %} performance = 'good' {% endif -%}
"""
template = Template(query_str)
query = template.render(product_stock=999)
log_query(question, query)

question = "What is the SQL query to select products based on category and price?"
query_str = """SELECT *
FROM products where 
{% if product_category == "Electronics" %}
    product_category = '{{ product_category }}' AND product_type = 
    {% if product_price > 500 %}
        'expensive' 
    {% else %}
        'normal'
    {% endif -%}
{% else -%}
    product_category = 'Others'
{% endif -%}
"""
template = Template(query_str)
query = template.render(product_category="Electronics", product_price=450)
log_query(question, query)

question = "What is the SQL query to select orders where order_id is in a given list?"
query_str = """SELECT *
FROM orders
WHERE order_id IN (
{% for order_id in order_ids %}
    {{ order_id }}{% if not loop.last %},{% endif -%}
{% endfor -%}
)"""
template = Template(query_str)
query = template.render(order_ids=[1234, 5678, 9012])
log_query(question, query)

question = "What is the SQL query to select orders based on nested project IDs and their associated order IDs?"
query_str = """SELECT *
FROM orders
WHERE order_id IN (
{% for project_id in project_ids %}
    {% for order_id in orders[project_id] %}
        {{ order_id }}{% if not loop.last %},{% endif -%}
    {% endfor -%}
{% endfor -%}
)"""
template = Template(query_str)
orders = {
    'project1': [1234, 5678],
    'project2': [9012, 3456],
    'project3': [7890]
}
query = template.render(project_ids=orders.keys(), orders=orders)
log_query(question, query)

question = "What is the SQL query to select users based on their username converted to lowercase?"
query_str = """SELECT *
FROM users
WHERE username = '{{ username | lower }}'"""
template = Template(query_str)
query = template.render(username='JOHN')
log_query(question, query)

question = "What is the SQL query to dynamically select columns from the users table?"
query_str = """
{% set columns = ['id', 'name', 'email', 'created_at'] %}
SELECT
{% for column in columns %}
    {{ column }}{% if not loop.last %}, {% endif -%}
{% endfor %}
FROM users
"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query to select from either 'orders' or 'orders_staging' based on production status?"
query_str = """
{% set table_name = 'orders' if is_production else 'orders_staging' %}
SELECT *
FROM {{ table_name }}
WHERE order_date >= '{{ start_date }}'
"""
template = Template(query_str)
query = template.render(is_production=True, start_date='2023-01-01')
log_query(question, query)

question = "What is the SQL query to filter orders based on a list of statuses?"
query_str = """
{% set status_list = ['pending', 'processing', 'shipped'] %}
SELECT *
FROM orders
WHERE status IN (
    {% for status in status_list %}
        '{{ status }}'{% if not loop.last %},{% endif -%}
    {% endfor -%}
)"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query that uses a macro to get the latest partition date from sales_data?"
query_str = """
{% macro get_latest_partition(table_name) %}
SELECT MAX(partition_date) FROM {{ table_name }}
{% endmacro %}

WITH latest_data AS (
{{ get_latest_partition('sales_data') }}
)
SELECT *
FROM sales_data
WHERE partition_date = (SELECT * FROM latest_data)"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query that dynamically pivots metrics based on a list of metrics?"
query_str = """
{% set metrics = ['revenue', 'cost', 'profit'] %}
SELECT
date,
{% for metric in metrics %}
    SUM(CASE WHEN metric_name = '{{ metric }}' THEN metric_value ELSE 0 END) AS {{ metric }}{% if not loop.last %},{% endif -%}
{% endfor -%}
FROM metrics_table
GROUP BY date"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query that generates UNION ALL queries for specific dates?"
query_str = """
{% set date_range = ['2023-01-01', '2023-02-01', '2023-03-01'] %}
{% for date in date_range %}
SELECT *
FROM orders
WHERE order_date = '{{ date }}'{% if not loop.last %} UNION ALL {% endif -%}
{% endfor %}
"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query that filters users based on a dynamic date column and days back parameter?"
query_str = """
{% set date_column = 'created_at' %}
{% set days_back = 30 %}
SELECT *
FROM users
WHERE {{ date_column }} >= DATEADD(day, -{{ days_back }}, CURRENT_DATE)"""
template = Template(query_str)
query = template.render()
log_query(question, query)

question = "What is the SQL query that conditionally aggregates sales data based on a grouping column?"
query_str = """
{% set group_by_column = 'category' if group_by_category else 'product_id' %}
SELECT
{{ group_by_column }},
SUM(sales_amount) AS total_sales
FROM sales
GROUP BY {{ group_by_column }}"""
template = Template(query_str)
query = template.render(group_by_category=True)
log_query(question, query)