import streamlit as st
import mysql.connector

# Database connection details
host = "localhost"
user = "your_username"
password = "your_password"
database = "your_database"

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
cursor = mydb.cursor()

# Streamlit app


def main():
    st.title("MySQL Database Connection")

    # Get user input
    query = st.text_area("Enter a SQL query")
    if st.button("Execute Query"):
        try:
            # Execute the SQL query
            cursor.execute(query)
            result = cursor.fetchall()

            # Display the query result
            if result:
                st.write("Query Result:")
                for row in result:
                    st.write(row)
            else:
                st.write("No data returned.")

        except mysql.connector.Error as err:
            st.error(f"Error executing query: {err}")


if __name__ == "__main__":
    main()
