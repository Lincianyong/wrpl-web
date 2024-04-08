# create_product_page.py
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

def create_product(productID, name, price, stock, seller, description):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc("create_product", (productID, name, price, stock, seller, description))
        connection.commit()

        st.success("Product created successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to create product: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def show():
    st.subheader("Add New Product")
    productID = st.text_input("Product ID")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0)
    stock = st.number_input("Stock", min_value=0)
    seller = st.text_input("Seller")
    description = st.text_area("Description")

    if st.button("Create Product"):
        if productID and name and price and stock and seller and description:
            create_product(productID, name, price, stock, seller, description)
        else:
            st.warning("Please fill in all fields")
