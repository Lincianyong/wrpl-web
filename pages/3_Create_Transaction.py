import streamlit as st
import mysql.connector

# Database connection details
def get_connection():
    return mysql.connector.connect(
        host="Alberts-MacBook-Pro.local",
        user="root",
        port="3306",
        password="10101011",
        database="eventjogja"
    )

# Stored procedure to create a new transaction
def create_transaction(buyer_id, event_id, buyer_phone, booking_date, booking_time, book_type_seat, book_price, book_vol, book_seat):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the stored procedure to create a new transaction
        cursor.callproc("create_new_transaction_3", [buyer_id, event_id, buyer_phone, booking_date, booking_time, book_type_seat, book_price, book_vol, book_seat])
        conn.commit()

        st.success("Transaction created successfully.")

    except mysql.connector.Error as err:
        st.error(f"Error creating transaction: {err}")

    finally:
        cursor.close()
        conn.close()

# Page title
st.title('Create New Transaction')

# User inputs for transaction details
buyer_id = st.text_input("Buyer ID:")
event_id = st.text_input("Event ID:")
buyer_phone = st.text_input("Buyer Phone:")
booking_date = st.date_input("Booking Date:")
booking_time = st.time_input("Booking Time:")
book_type_seat = st.selectbox("Booking Type Seat", ["Regular", "VIP", "VVIP"])
book_price = st.number_input("Booking Price:")
book_vol = st.number_input("Booking Volume:")
book_seat = st.text_input("Booking Seat:")

# Create transaction button
if st.button("Create Transaction"):
    if buyer_id and event_id and buyer_phone and booking_date and booking_time and book_type_seat and book_price and book_vol and book_seat:
        create_transaction(buyer_id, event_id, buyer_phone, booking_date, booking_time, book_type_seat, book_price, book_vol, book_seat)
    else:
        st.warning("Please fill in all fields.")
