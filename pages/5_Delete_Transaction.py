import streamlit as st
import mysql.connector

# Database connection details
def get_connection():
    return mysql.connector.connect(
        host="Alberts-MacBook-Pro.local",
        user="root",
        port="3306",
        password="10101011",
        database="eventjogja"
    )

# Stored procedure to delete transaction by ID
def delete_transaction_by_id(transaction_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the stored procedure to delete transaction by ID
        cursor.callproc("delete_transaction_by_id", [transaction_id])
        conn.commit()

        st.success("Transaction deleted successfully.")

    except mysql.connector.Error as err:
        st.error(f"Error deleting transaction: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('Delete Transaction')

# User input for transaction ID
transaction_id = st.text_input("Enter Transaction ID:")

# Delete transaction button
if st.button("Delete Transaction"):
    if transaction_id:
        delete_transaction_by_id(transaction_id)
    else:
        st.warning("Please enter a Transaction ID.")
