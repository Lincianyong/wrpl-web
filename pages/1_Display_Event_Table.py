import streamlit as st
import mysql.connector
import pandas as pd

# Database connection details
def get_connection():
    return mysql.connector.connect(
        host="Alberts-MacBook-Pro.local",
        user="root",
        port="3306",
        password="10101011",
        database="eventjogja"
    )

def display_tbEventMaster():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Retrieve data from tbEventMaster table
        cursor.execute("SELECT * FROM tbEventMaster")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Display the table
        st.subheader("tbEventMaster Table")
        st.write(f"Showing {len(df)} rows")
        st.dataframe(df)

    except mysql.connector.Error as err:
        st.error(f"Error displaying tbEventMaster table: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('Event Master Table Display')

# Display tbEventMaster table
display_tbEventMaster()
