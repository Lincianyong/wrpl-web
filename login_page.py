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

def login(username, password):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Execute SQL query to check if customer exists
        query = "SELECT COUNT(*) FROM customers WHERE name = %s AND customerID = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result[0] == 1:
            st.success("Login successful")
            # Display customer's transactions and products
            display_customer_data(username, cursor)  # Pass username and cursor to display customer's data
        else:
            st.error("Invalid username or password")
    except mysql.connector.Error as error:
        st.error(f"Failed to login: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def display_customer_data(username, cursor):
    try:
        st.subheader("Customer Information")
        # Retrieve customer data
        query_customer = "SELECT * FROM customers WHERE name = %s"
        cursor.execute(query_customer, (username,))
        customer_data = cursor.fetchone()
        if customer_data:
            customer_id, name, address = customer_data
            st.write(f"Customer ID: {customer_id}")
            st.write(f"Name: {name}")
            st.write(f"Address: {address}")
            st.write("---")

            # Retrieve customer's transactions
            query_transactions = """
            SELECT t.transactionID, p.name AS product_name, SUM(ti.price) AS totalPrice, s.companyName
            FROM transactions t
            INNER JOIN transaction_items ti ON t.transactionID = ti.transactionID
            INNER JOIN products p ON ti.productID = p.productID
            INNER JOIN shippings s ON t.shippingID = s.shippingID
            WHERE t.customerID = %s
            GROUP BY t.transactionID, p.name, s.companyName
            """
            cursor.execute(query_transactions, (customer_id,))
            transactions = cursor.fetchall()
            if transactions:
                st.subheader("Transactions")
                for transaction in transactions:
                    transaction_id, product_name, total_price, company_name = transaction
                    st.write(f"Transaction ID: {transaction_id}")
                    st.write(f"Product Name: {product_name}")
                    st.write(f"Total Price: {total_price}")
                    st.write(f"Shipping Company: {company_name}")
                    st.write("---")
            else:
                st.write("No transactions found for this customer")
        else:
            st.error("Customer not found")
    except mysql.connector.Error as error:
        st.error(f"Failed to display customer data: {error}")

def show():
    st.subheader("Login")
    username = st.text_input("Name")
    password = st.text_input("CustomerID", type="password")
    if st.button("Login"):
        if username and password:
            login(username, password)
        else:
            st.warning("Please fill in all fields")