import streamlit as st
from db import get_cursor

def user_auth():
    cursor = get_cursor()

    st.subheader("User Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        # Code to authenticate the user
        query = "SELECT * FROM customers WHERE name = %s AND address = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")

    st.subheader("User Signup")
    signup_username = st.text_input("Enter Username")
    signup_password = st.text_input("Enter Password", type="password")
    signup_confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        # Code to handle user signup
        if signup_password == signup_confirm_password:
            query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            values = (signup_username, signup_password)
            cursor.execute(query, values)
            cursor.connection.commit()
            st.success("User registered successfully!")
        else:
            st.error("Passwords do not match.")

    st.subheader("Change User Details")
    change_username = st.text_input("Enter Username")
    change_password = st.text_input("Enter New Password", type="password")
    change_confirm_password = st.text_input("Confirm New Password", type="password")

    if st.button("Change User Details"):
        # Code to allow users to change their details
        if change_password == change_confirm_password:
            query = "UPDATE customers SET name = %s, address = %s WHERE name = %s"
            values = (change_username, change_password, change_username)
            cursor.execute(query, values)
            cursor.connection.commit()
            st.success("User details updated successfully!")
        else:
            st.error("Passwords do not match.")