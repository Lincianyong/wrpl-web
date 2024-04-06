# import streamlit as st
# from pages import (
#     user_auth,
# #     create_transaction,
# #     remove_transaction,
# #     transaction_history,
# #     catalog,
# #     product_management,
# )

# def main():
#     st.title("E-commerce Application")
#     option = st.sidebar.selectbox("Select a Page", [
#         "User Authentication",
#         "Create Transaction",
#         "Remove Transaction",
#         "Transaction History",
#         "Product Catalog",
#         "Product Management",
#     ])

#     if option == "User Authentication":
#         user_auth.user_auth()
#     elif option == "Create Transaction":
#         create_transaction.create_transaction()
#     elif option == "Remove Transaction":
#         remove_transaction.remove_transaction()
#     elif option == "Transaction History":
#         transaction_history.user_transaction_history()
#     elif option == "Product Catalog":
#         catalog.display_catalog()
#     elif option == "Product Management":
#         product_management.product_management()

# if __name__ == "__main__":
#     main()