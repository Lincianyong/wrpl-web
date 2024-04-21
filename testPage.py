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

# Function to call SQL procedure to get transaction by ID
def get_transaction_by_id(transaction_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetTransactionNew", [transaction_id])
    
    # Iterate over the generator to get the cursor containing the result set
    for result in cursor.stored_results():
        transaction = result.fetchone()
    
    conn.close()
    return transaction

# Main function to display transaction by ID
def main():
    st.title("Find Transaction by ID")
    
    # Input field for transaction ID
    transaction_id = st.text_input("Enter Transaction ID:")
    
    if st.button("Search"):
        if transaction_id:
            # Call function to get transaction by ID
            transaction = get_transaction_by_id(transaction_id)
            
            if transaction:
                st.write("Transaction Found:")
                st.write(transaction)
            else:
                st.write("Transaction not found.")
        else:
            st.write("Please enter a transaction ID.")

if __name__ == "__main__":
    main()
