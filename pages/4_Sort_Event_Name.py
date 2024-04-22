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

# Stored procedure to sort events by name
def sort_events_by_name():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the stored procedure to sort events by name
        cursor.callproc("sort_events_by_name")
        
        # Fetch the result
        for result in cursor.stored_results():
            data = result.fetchall()
            columns = [desc[0] for desc in result.description]

            # Convert data to a pandas DataFrame
            df = pd.DataFrame(data, columns=columns)

            # Display the result
            if len(df) == 0:
                st.write("No events found.")
            else:
                st.subheader("Sorted Events by Name")
                st.write(df)

    except mysql.connector.Error as err:
        st.error(f"Error sorting events: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('Sorted Events by Name')

# Display sorted events
sort_events_by_name()
