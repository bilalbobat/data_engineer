"""
Question: How can I implement a logging mechanism in a Python application to log SQL queries, including the setup for a log file named app.log, 
configuring the logging level to INFO, specifying a custom format for log messages '%(asctime)s - %(levelname)s - %(message)s', and ensuring 
that the log file is overwritten each time the application runs? 

Additionally, how can I create a function to log both the question and the corresponding SQL query?
"""

# Remove
import logging

# Remove
def log_query(question, query):
    logging.info(f"\n{question}\n{query}")

# Remove
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
query = template.render()
log_query(question, query)

question = """Question: Write a SQL query to calculate the 'running total' of 'sales_amount' for each 'product_category' 
ensuring that the results are ordered by 'sale_date'? Return the 'product_category', 'sales_amount', and 'running_total' in the output.
"""
# Remove
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
# Remove
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
# Remove
query_str = "SELECT * FROM orders WHERE product = '{{ product }}' AND quantity >= {{ min_quantity }}"
template = Template(query_str)
query = template.render(product='Laptop', min_quantity=5)
log_query(question, query)

question = "What is the SQL query to select all users and conditionally filter by user_age only if user_age is 18 or older?"
# Remove
query_str = """SELECT * FROM users {% if user_age >= 18 %} WHERE age >= {{ user_age }}{% endif -%};"""
template = Template(query_str)
query = template.render(user_age=18)
log_query(question, query)

question = "What is the SQL query to select orders where order_id is in a given list?"
# Remove
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