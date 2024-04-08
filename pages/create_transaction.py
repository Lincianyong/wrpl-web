import streamlit as st
import mysql.connector
import datetime
import random

host = "localhost"
user = "root"
password = "RINNEA098123/#"
database = "ecommerce"

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RINNEA098123/#",
        database="ecommerce"
    )

def create_transaction(customer_id, transaction_date, transaction_status, shipping_id, product_items, total_price):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Insert transaction into the transactions table
        query = "INSERT INTO transactions (transactionID, transactionDate, transactionStatus, customerID, shippingID, totalPrice) VALUES (%s, %s, %s, %s, %s, %s)"
        transaction_id = generate_transaction_id()
        values = (transaction_id, transaction_date, transaction_status, customer_id, shipping_id, total_price)
        cursor.execute(query, values)

        # Insert product items into the transaction_items table
        for item in product_items:
            query = "INSERT INTO transaction_items (transactionID, productID, quantity, price) VALUES (%s, %s, %s, %s)"
            values = (transaction_id, item['product_id'], item['quantity'], item['price'])
            cursor.execute(query, values)

        conn.commit()
        st.success(f"Transaction created successfully! Transaction ID: {transaction_id}, Total Price: {total_price}")

    except mysql.connector.Error as error:
        st.error(f"Failed to create transaction: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT productID, name, price FROM products"
        cursor.execute(query)
        products = cursor.fetchall()

        return products

    except mysql.connector.Error as error:
        st.error(f"Failed to fetch products: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_shipping_companies():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT shippingID, companyName, fee FROM shippings"
        cursor.execute(query)
        shipping_companies = cursor.fetchall()

        return shipping_companies

    except mysql.connector.Error as error:
        st.error(f"Failed to fetch shipping companies: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def generate_transaction_id():
    # Generate a unique transaction ID (you can use your own logic here)
    # For example, you can use a combination of a prefix and a random number
    transaction_id = f"T{random.randint(1000, 9999)}"
    return transaction_id

def show():
    st.title("Create Transaction")

    customer_id = st.text_input("Customer ID")
    transaction_date = st.date_input("Transaction Date")
    transaction_status = "Pending"

    products = get_products()
    product_items = []
    total_price = 0

    # Display product selection and quantity input fields
    for product in products:
        product_id = product[0]
        product_name = product[1]
        product_price = product[2]

        quantity = st.number_input(f"Quantity for {product_name}", min_value=0, value=0, step=1)

        if quantity > 0:
            item_price = quantity * product_price
            item = {
                'product_id': product_id,
                'quantity': quantity,
                'price': product_price  # Use the price from the products table
            }
            product_items.append(item)
            total_price += item_price

    shipping_companies = get_shipping_companies()
    shipping_options = [f"{company[1]} - Fee: {company[2]}" for company in shipping_companies]
    selected_shipping = st.selectbox("Select Shipping Company", shipping_options)
    shipping_id = shipping_companies[shipping_options.index(selected_shipping)][0]

    if st.button("Create Transaction"):
        if customer_id and transaction_date and len(product_items) >= 1:
            create_transaction(customer_id, transaction_date, transaction_status, shipping_id, product_items, total_price)
        else:
            st.warning("Please fill in all the required fields and select at least one product.")