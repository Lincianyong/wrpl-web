import streamlit as st
import mysql.connector
import pandas as pd

st.title("Welcome to Event Jogja")

# Database connection details
def get_connection():
    return mysql.connector.connect(
        host="Alberts-MacBook-Pro.local",
        user="root",
        port="3306",
        password="10101011",
        database="eventjogja"
    )

# Function to get all tables in the database
def get_tables():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Get all tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tables = [table[0] for table in tables]

        return tables

    except mysql.connector.Error as err:
        st.error(f"Error getting tables: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('All Tables in the Database')

# Get all tables in the database
tables = get_tables()

# Display all tables
if tables:
    for table in tables:
        st.subheader(f"Table: {table}")
        df = pd.read_sql(f"SELECT * FROM {table}", con=get_connection())
        st.write(df)
else:
    st.error("No tables found in the database.")
