import streamlit as st
import mysql.connector

# Database connection parameters
host = "localhost"
user = "root"
port = "3307"
password = "RINNEA098123/#"
database = "ecommerce"

# Function to establish database connection
def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=database
    )

# Function to fetch all customers from the database
def fetch_customers():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

# Page title
st.title('List of Customers')

# Fetch customers from the database
customers = fetch_customers()

# Display customers in a table
if customers:
    st.table(customers)
else:
    st.write('No customers found')
