import streamlit as st
import mysql.connector

# Set page name
st.title("Add Customer")

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

# Function to check if customer exists
def customer_exists(customerID):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM customers WHERE customerID = %s", (customerID,))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count > 0

# Function to add a new customer using the stored procedure
def add_customer(customerID, customerName, customerAddress):
    if not customer_exists(customerID):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.callproc("AddCustomer", (customerID, customerName, customerAddress))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    else:
        return False

# Form to input new customer details
customerID = st.text_input('Customer ID')
customerName = st.text_input('Customer Name')
customerAddress = st.text_input('Customer Address')

# Button to add customer
if st.button('Add Customer'):
    if customerID and customerName and customerAddress:
        if add_customer(customerID, customerName, customerAddress):
            st.success('Customer added successfully.')
        else:
            st.error('Customer with the same ID already exists.')
    else:
        st.error('Please fill in all the fields.')