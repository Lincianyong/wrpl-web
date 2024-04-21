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

# Function to fetch all transactions
def fetch_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

# Main function to display transactions
def main():
    st.title("Transactions Table")
    
    # Fetch transactions from the database
    transactions = fetch_transactions()
    
    # Display transactions in a table
    if transactions:
        st.table(transactions)
    else:
        st.write("No transactions found.")

if __name__ == "__main__":
    main()
