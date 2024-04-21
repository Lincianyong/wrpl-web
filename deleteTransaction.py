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

# Function to delete a transaction using the stored procedure
def delete_transaction(transactionID):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc("DeleteTransaction", (transactionID,))
    connection.commit()
    cursor.close()
    connection.close()

# Page title
st.title('Delete Transaction')

# Form to input transaction ID
transactionID = st.text_input('Transaction ID')

# Button to delete transaction
if st.button('Delete Transaction'):
    if transactionID:
        delete_transaction(transactionID)
        st.success('Transaction deleted successfully.')
    else:
        st.error('Please enter a transaction ID.')
