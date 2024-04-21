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

# Function to add a new customer using the stored procedure
def add_customer(customerID, customerName, customerAddress):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc("AddCustomer", (customerID, customerName, customerAddress))
    connection.commit()
    cursor.close()
    connection.close()

# Page title
st.title('Add New Customer')

# Form to input new customer details
customerID = st.text_input('Customer ID')
customerName = st.text_input('Customer Name')
customerAddress = st.text_input('Customer Address')

# Button to add customer
if st.button('Add Customer'):
    if customerID and customerName and customerAddress:
        add_customer(customerID, customerName, customerAddress)
        st.success('Customer added successfully.')
    else:
        st.error('Please fill in all the fields.')
