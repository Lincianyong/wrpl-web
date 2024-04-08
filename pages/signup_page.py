# signup_page.py
import streamlit as st
import mysql.connector

# Database connection details
host = "localhost"
user = "root"
password = "RINNEA098123/#"
database = "ecommerce"

def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Define the stored procedure call function for sign-up
def signup(customerID, name, address):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc("signup", (customerID, name, address))
        connection.commit()

        st.success("Sign-up successful")

    except mysql.connector.Error as error:
        st.error(f"Failed to sign up: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to display the sign-up form
def show():
    st.subheader("Sign Up")
    customerID = st.text_input("Customer ID")
    name = st.text_input("Name")
    address = st.text_input("Address")

    if st.button("Sign Up"):
        if customerID and name and address:
            signup(customerID, name, address)
        else:
            st.warning("Please fill in all fields")
