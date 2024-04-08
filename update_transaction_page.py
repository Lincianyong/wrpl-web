# update_transaction_page.py
import streamlit as st
import mysql.connector

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

def update_transaction_status(transaction_id, new_status):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Call the stored procedure to update the transaction status
        cursor.callproc("update_transaction_status", [transaction_id, new_status])

        # Fetch the result returned by the stored procedure
        result = next(cursor.stored_results())
        message = result.fetchone()[0]

        st.success(message)

        connection.commit()
    except mysql.connector.Error as error:
        st.error(f"Failed to update transaction status: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def show():
    st.title("Update Transaction Status")

    transaction_id = st.text_input("Transaction ID")
    new_status = st.selectbox("New Status", ["Completed", "Cancelled"])

    if st.button("Update"):
        if transaction_id:
            update_transaction_status(transaction_id, new_status)
        else:
            st.warning("Please enter a transaction ID")