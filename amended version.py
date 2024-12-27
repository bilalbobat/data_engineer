from jinja2 import Template
import logging

logging.basicConfig(
    filename='app.log',  # Specify the file name
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the format of log messages
    filemode='w'  # Set filemode to 'w' to overwrite the log file
)

# Using Variables in SQL Query:
query_str = "SELECT * FROM {{ table_name }}"
template = Template(query_str)
query = template.render(table_name="users")
print(query)
logging.info(query)

# Multiple Variables in SQL Query
query_str = "SELECT * FROM orders WHERE product = '{{ product }}' AND quantity >= {{ min_quantity }}"
template = Template(query_str)
query = template.render(product='Laptop', min_quantity=5)
print(query)
logging.info(query)

# Using Conditional If Statements in SQL Query
query_str = """SELECT * FROM users {% if user_age >= 18 %}WHERE age >= {{ user_age }}{% endif -%};"""
template = Template(query_str)
query = template.render(user_age=30)
print(query)
logging.info(query)

# Using If-Else Statements in SQL Query
query_str = """SELECT * FROM users WHERE{% if user_age >= 18 %} adult >= True {% else %} adult = False {% endif -%};"""
template = Template(query_str)
query = template.render(user_age=30)
print(query)
logging.info(query)

# Using If-Elif-Else Statements in SQL Query
query_str = """SELECT * FROM products where
{% if product_stock >= 1000 %} performance = 'bad' 
{% elif product_stock >= 300 and product_stock < 1000 %} performance = 'average' 
{% else %} performance = 'good' {% endif -%}
"""
template = Template(query_str)
query = template.render(product_stock=999)
print(query)
logging.info(query)

# Nested If Statements in SQL Query
query_str = """SELECT *
FROM products where 
{% if product_category == "Electronics" %}
    product_category = '{{ product_category }}'
    {% if product_price > 500 %}
        product_type = 'expensive' 
    {% else %}
        product_type = 'normal'
    {% endif -%}
{% else -%}
    product_category = 'Others'
{% endif -%}
"""
template = Template(query_str)
query = template.render(product_category="Electronics", product_price=450)
print(query)
logging.info(query)

# Using For Loop in SQL Query
query_str = """SELECT *
FROM orders
WHERE order_id IN (
{% for order_id in order_ids %}
    {{ order_id }}{% if not loop.last %},{% endif -%}
{% endfor -%}
)"""
template = Template(query_str)
query = template.render(order_ids=[1234, 5678, 9012])
print(query)
logging.info(query)

# Using nested for loop
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
print(query)
logging.info(query)

# Built-in Filter of Jinja templates
query_str = """SELECT *
FROM users
WHERE username = '{{ username | lower }}'"""
template = Template(query_str)
query = template.render(username='JOHN')
print(query)
logging.info(query)

# Dynamic column selection
query_str = """
{% set columns = ['id', 'name', 'email', 'created_at'] %}
SELECT
{% for column in columns %}
    {{ column }}{% if not loop.last %},{% endif -%}
{% endfor %}
FROM users
"""
template = Template(query_str)
query = template.render()
print(query)
logging.info(query)

# Conditional table selection
query_str = """
{% set table_name = 'orders' if is_production else 'orders_staging' %}
SELECT *
FROM {{ table_name }}
WHERE order_date >= '{{ start_date }}'
"""
template = Template(query_str)
query = template.render(is_production=True, start_date='2023-01-01')
print(query)
logging.info(query)

# Dynamic filtering based on a list of values
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
print(query)
logging.info(query)

# Using macros for reusable code
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
print(query)
logging.info(query)

# Dynamic pivoting
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
print(query)
logging.info(query)

# Generating UNION ALL queries
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
print(query)
logging.info(query)

# Dynamic date filtering
query_str = """
{% set date_column = 'created_at' %}
{% set days_back = 30 %}
SELECT *
FROM users
WHERE {{ date_column }} >= DATEADD(day, -{{ days_back }}, CURRENT_DATE)"""
template = Template(query_str)
query = template.render()
print(query)
logging.info(query)

# Conditional aggregation
query_str = """
{% set group_by_column = 'category' if group_by_category else 'product_id' %}
SELECT
{{ group_by_column }},
SUM(sales_amount) AS total_sales
FROM sales
GROUP BY {{ group_by_column }}"""
template = Template(query_str)
query = template.render(group_by_category=True)
print(query)
logging.info(query)

