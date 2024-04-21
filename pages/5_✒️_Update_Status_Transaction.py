import streamlit as st
import mysql.connector

# Function to get database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3307",
        password="RINNEA098123/#",
        database="ecommerce"
    )

# Function to update transaction status
def update_transaction_status(transactionID, new_status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Ensure collation consistency by converting transactionID to binary
        cursor.execute("UPDATE transactions SET transactionStatus = %s WHERE BINARY transactionID = %s", (new_status, transactionID))
        
        conn.commit()
        st.success('Transaction status updated successfully.')
    except mysql.connector.Error as err:
        st.error(f"Error updating transaction status: {err}")
    finally:
        cursor.close()
        conn.close()

# Streamlit app
def main():
    st.title('Update Transaction Status')

    # Form for updating transaction status
    transaction_id = st.text_input('Transaction ID', max_chars=255)
    new_status = st.selectbox('New Status', ['Completed', 'Pending', 'Canceled'])

    # Button to trigger update
    if st.button('Update Status'):
        if not transaction_id:
            st.warning('Please enter a transaction ID.')
        else:
            update_transaction_status(transaction_id, new_status)

if __name__ == "__main__":
    main()