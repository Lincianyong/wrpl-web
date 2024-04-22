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

# SQL procedure to search event by eventID
def search_event(event_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the SQL procedure to search for the event
        cursor.callproc("search_event_by_id", [event_id])
        
        # Fetch the result
        for result in cursor.stored_results():
            data = result.fetchall()
            columns = [desc[0] for desc in result.description]

            # Convert data to a pandas DataFrame
            df = pd.DataFrame(data, columns=columns)

            # Display the result
            if len(df) == 0:
                st.write("Event not found.")
            else:
                st.subheader("Search Result")
                st.write(df)

    except mysql.connector.Error as err:
        st.error(f"Error searching event: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('Event Search')

# User input for event ID
event_id = st.text_input("Enter Event ID:")

# Search button
if st.button("Search"):
    if event_id:
        search_event(event_id)
    else:
        st.warning("Please enter an Event ID.")
