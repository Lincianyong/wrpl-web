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

# # Function to delete a transaction using the stored procedure
# def delete_transaction(transactionID):
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.callproc("DeleteTransaction", (transactionID,))
#     connection.commit()
#     cursor.close()
#     connection.close()

# # Page title
# st.title('Delete Transaction')

# # Form to input transaction ID
# transactionID = st.text_input('Transaction ID')

# # Button to delete transaction
# if st.button('Delete Transaction'):
#     if transactionID:
#         delete_transaction(transactionID)
#         st.success('Transaction deleted successfully.')
#     else:
#         st.error('Please enter a transaction ID.')

# Function to delete a transaction by its ID
def delete_transaction_by_id(transaction_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc("DeleteTransactionByID", [transaction_id])
    connection.commit()
    cursor.close()
    connection.close()

# Streamlit app to delete a transaction
def main():
    st.title("Delete Transaction by ID")

    # Input field for transaction ID
    transaction_id = st.text_input("Enter Transaction ID:")

    # Button to delete transaction
    if st.button("Delete Transaction"):
        if transaction_id:
            # Call function to delete transaction by ID
            delete_transaction_by_id(transaction_id)
            st.success(f"Transaction with ID {transaction_id} deleted successfully.")
        else:
            st.error("Please enter a transaction ID.")

if __name__ == "__main__":
    main()