# import streamlit as st
# import mysql.connector
# import pandas as pd

# # Database connection details
# host = "localhost"
# user = "root"
# password = "RINNEA098123/#"
# database = "ecommerce"

# def get_connection():
#     return mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

# def display_tables():
#     st.title("Database Tables")

#     # Create a sidebar for table selection
#     table_name = st.sidebar.selectbox("Select a Table", ["customers", "products", "shippings", "transactions", "transaction_items"])

#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT * FROM {table_name}")
#         data = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]

#         # Convert data to a pandas DataFrame
#         df = pd.DataFrame(data, columns=columns)

#         # Display the table
#         st.subheader(f"{table_name.capitalize()} Table")
#         st.write(f"Showing {len(df)} rows")
#         st.dataframe(df)

#     except mysql.connector.Error as err:
#         st.error(f"Error displaying table: {err}")

#     finally:
#         cursor.close()
#         conn.close()

# display_tables()

import streamlit as st
import mysql.connector
import pandas as pd

# Database connection details
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3307",
        password="RINNEA098123/#",
        database="ecommerce"
    )

def display_table(table_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Display the table
        st.subheader(f"{table_name.capitalize()} Table")
        st.write(f"Showing {len(df)} rows")
        st.dataframe(df)

    except mysql.connector.Error as err:
        st.error(f"Error displaying table: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('E-commerce Dashboard')

# Sidebar options
options = ["Customers", "Products", "Shippings", "Transactions"]
selected_option = st.sidebar.selectbox("Select an option", options)

# Display selected option
if selected_option == "Customers":
    display_table("customers")
elif selected_option == "Products":
    display_table("products")
elif selected_option == "Shippings":
    display_table("shippings")
elif selected_option == "Transactions":
    display_table("transactions")