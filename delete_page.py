# delete_page.py
import streamlit as st
import mysql.connector

host = "localhost"
user = "root"
port = "3007"
password = "RINNEA098123/#"
database = "ecommerce"

def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=database
    )

def delete_transaction(transaction_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Call the stored procedure to delete the transaction
        cursor.callproc("delete_transaction", [transaction_id])

        # Fetch the result returned by the stored procedure
        result = next(cursor.stored_results())
        message = result.fetchone()[0]

        if "has been deleted" in message:
            st.success(message)
        else:
            st.warning(message)

        connection.commit()
    except mysql.connector.Error as error:
        st.error(f"Failed to delete transaction: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def show():
    st.title("Delete Transaction")
    transaction_id = st.text_input("Transaction ID")
    if st.button("Delete"):
        if transaction_id:
            delete_transaction(transaction_id)
        else:
            st.warning("Please enter a transaction ID")