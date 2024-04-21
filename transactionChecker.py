import streamlit as st
import mysql.connector

# Function to get database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3307",
        password="RINNEA098123/#",
        database="ecommerce"
    )

# Function to call SQL procedure to get transaction details by ID
def get_transaction_details(transaction_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetTransactionDetails", [transaction_id])
    result = cursor.stored_results()
    transaction_details = result.fetchone()
    conn.close()
    return transaction_details

# Main function to display transaction details by ID
def main():
    st.title("Find Transaction Details by ID")
    
    # Input field for transaction ID
    transaction_id = st.text_input("Enter Transaction ID:")
    
    if st.button("Search"):
        if transaction_id:
            # Call function to get transaction details by ID
            transaction_details = get_transaction_details(transaction_id)
            
            if transaction_details:
                st.write("Transaction Details Found:")
                st.write("Customer Name:", transaction_details[0])
                st.write("Shipping Company:", transaction_details[1])
            else:
                st.write("Transaction not found.")
        else:
            st.write("Please enter a transaction ID.")

if __name__ == "__main__":
    main()
