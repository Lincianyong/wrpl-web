import streamlit as st
import pandas as pd

# Sample customer data
customer_data = {
    'customerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010',
                   'C011', 'C012', 'C013', 'C014', 'C015', 'C016', 'C017', 'C018', 'C019', 'C020'],
    'name': ['John Doe', 'Alice Smith', 'Bob Johnson', 'Emily Brown', 'David Wilson', 'Sarah Jones',
             'Michael Davis', 'Emma Taylor', 'Christopher Martinez', 'Olivia Rodriguez', 'William Hernandez',
             'Sophia Lopez', 'James Gonzalez', 'Isabella Perez', 'Alexander Torres', 'Mia Rivera', 'Daniel Moore',
             'Charlotte Sanchez', 'Benjamin Bennett', 'Ava Powell'],
    'password': ['password1', 'password2', 'password3', 'password4', 'password5', 'password6',
                 'password7', 'password8', 'password9', 'password10', 'password11', 'password12',
                 'password13', 'password14', 'password15', 'password16', 'password17', 'password18',
                 'password19', 'password20']
}

# Sample transaction data
transaction_data = {
    'transactionID': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008', 'T009', 'T010',
                      'T011', 'T012', 'T013', 'T014', 'T015', 'T016', 'T017', 'T018', 'T019', 'T020'],
    'transactionDate': ['2024-03-20', '2024-03-20', '2024-03-21', '2024-03-21', '2024-03-22',
                        '2024-03-22', '2024-03-23', '2024-03-23', '2024-03-24', '2024-03-24',
                        '2024-03-25', '2024-03-25', '2024-03-26', '2024-03-26', '2024-03-27',
                        '2024-03-27', '2024-03-28', '2024-03-28', '2024-03-29', '2024-03-29'],
    'transactionStatus': ['Completed', 'Pending', 'Completed', 'Pending', 'Completed',
                          'Completed', 'Pending', 'Completed', 'Pending', 'Completed',
                          'Pending', 'Completed', 'Pending', 'Completed', 'Pending',
                          'Completed', 'Pending', 'Completed', 'Pending', 'Completed'],
    'transactionPrice': [8500000, 15000000, 7200000, 1500000, 6000000,
                         12500000, 3000000, 800000, 10000000, 9500000,
                         12000000, 3800000, 9000000, 2200000, 1200000,
                         1700000, 900000, 4500000, 750000, 1200000],
    'customerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010',
                   'C011', 'C012', 'C013', 'C014', 'C015', 'C016', 'C017', 'C018', 'C019', 'C020']
}

# Create DataFrame for customer and transaction data
customer_df = pd.DataFrame(customer_data)
transaction_df = pd.DataFrame(transaction_data)

# Page title
st.title('Login Page')

# Username and password inputs
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    # Check if username and password match
    if username in customer_df['name'].values:
        customer_id = customer_df.loc[customer_df['name']
                                      == username, 'customerID'].iloc[0]
        correct_password = customer_df.loc[customer_df['name']
                                           == username, 'password'].iloc[0]
        if password == correct_password:
            st.success("Login successful!")
            st.write(
                f"Welcome, {username}! Your Customer ID is: {customer_id}")

            # Display transactions for the customer
            st.write("**Your Transactions**")
            customer_transactions = transaction_df[transaction_df['customerID'] == customer_id]
            st.write(customer_transactions)

            # Calculate total spending
            total_spending = customer_transactions['transactionPrice'].sum()
            st.write(f"**Total Spending**: ${total_spending}")
        else:
            st.error("Incorrect password. Please try again.")
    else:
        st.error("Username not found. Please try again.")
