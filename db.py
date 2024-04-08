import streamlit as st
import signup_page, create_product_page, login_page, delete_page, update_transaction_page, create_transaction

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

    # Define options in the sidebar
    st.sidebar.title("Pages")
    selected_page = st.sidebar.selectbox("Select Page", ["Sign Up", "Sign In", "Create Product", "Delete Transaction", "Update Transaction Status", "Create Transaction"])

    # Display selected page
    if selected_page == "Sign Up":
        signup_page.show()
    elif selected_page == "Sign In":
        login_page.show()
    elif selected_page == "Create Product":
        create_product_page.show()
    elif selected_page == "Delete Transaction":
        delete_page.show()
    elif selected_page == "Update Transaction Status":
        update_transaction_page.show()
    elif selected_page == "Create Transaction":
        create_transaction.show()

if __name__ == "__main__":
    main()