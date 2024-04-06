import streamlit as st
import mysql.connector

# Database connection details
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

def main():
    st.title("E-commerce Application")

    # Check if the customer is logged in
    if "customer" not in st.session_state:
        handle_login_or_signup()
    else:
        # Customer is logged in, show main page
        st.sidebar.success(f"Logged in as {st.session_state.customer['name']}")
        # Add your main page content here
        # ...
        create_transaction()

def handle_login_or_signup():
    login_or_signup = st.sidebar.selectbox("Login or Signup", ["Login", "Signup"])

    if login_or_signup == "Login":
        handle_customer_login()
    else:
        handle_customer_signup()

def handle_customer_login():
    with st.form("login_form"):
        customer_id = st.text_input("Customer ID")
        login_button = st.form_submit_button("Login")

        if login_button:
            conn = None
            cursor = None
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.callproc("sp_customer_login", [customer_id])
                customer = cursor.fetchone()

                if customer:
                    customer_data = {
                        'customerID': customer[0],
                        'name': customer[1],
                        'address': customer[2]
                    }
                    st.session_state["customer"] = customer_data
                    st.success("Login successful!")

                    # Print customer details
                    print("Customer Details:")
                    print(f"Customer ID: {customer_data['customerID']}")
                    print(f"Name: {customer_data['name']}")
                    print(f"Address: {customer_data['address']}")
                else:
                    st.error("Invalid customer ID")

            except mysql.connector.Error as err:
                st.error(f"Error logging in: {err}")
                print(f"Error logging in: {err}")

            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()


def handle_customer_signup():
    with st.form("signup_form"):
        customerID = st.text_input("Enter ID")
        name = st.text_input("Enter name")
        address = st.text_input("Enter address")
        signup_button = st.form_submit_button("Signup")

        if signup_button:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.callproc("sp_create_customer", [customerID, name, address])
                conn.commit()
                st.success("Customer Created")
            except mysql.connector.Error as err:
                st.error(f"Error creating customer: {err}")
            finally:
                cursor.close()
                conn.close()


def create_transaction():
    with st.form("transaction_form"):
        transaction_id = st.text_input("Enter Transaction ID")
        customer_id = st.session_state.customer['customerID']
        shipping_id = st.text_input("Enter Shipping ID")
        create_transaction_button = st.form_submit_button("Create Transaction")

        if create_transaction_button:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.callproc("sp_create_transaction", [transaction_id, customer_id, shipping_id])
                conn.commit()
                st.success("Transaction created successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error creating transaction: {err}")
            finally:
                cursor.close()
                conn.close()

if __name__ == "__main__":
    main()