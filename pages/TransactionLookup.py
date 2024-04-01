import streamlit as st
import pandas as pd

# Sample data
customers_data = {
    'customerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010',
                   'C011', 'C012', 'C013', 'C014', 'C015', 'C016', 'C017', 'C018', 'C019', 'C020'],
    'name': ['John Doe', 'Alice Smith', 'Bob Johnson', 'Emily Brown', 'David Wilson', 'Sarah Jones',
             'Michael Davis', 'Emma Taylor', 'Christopher Martinez', 'Olivia Rodriguez', 'William Hernandez',
             'Sophia Lopez', 'James Gonzalez', 'Isabella Perez', 'Alexander Torres', 'Mia Rivera',
             'Daniel Moore', 'Charlotte Sanchez', 'Benjamin Bennett', 'Ava Powell'],
    'address': ['123 Main Street', '456 Elm Street', '789 Oak Avenue', '101 Pine Road', '202 Maple Lane',
                '303 Cedar Street', '404 Birch Drive', '505 Willow Court', '606 Pineapple Avenue', '707 Elmwood Lane',
                '808 Oakwood Drive', '909 Cedar Avenue', '1010 Maple Road', '1111 Pinecrest Boulevard', '1212 Willow Street',
                '1313 Oakcrest Avenue', '1414 Cedar Lane', '1515 Elm Drive', '1616 Oakwood Court', '1717 Maple Avenue']
}

products_data = {
    'productID': ['P00-001', 'P00-002', 'P00-003', 'P00-004', 'P00-005', 'P00-006', 'P00-007', 'P00-008', 'P00-009', 'P00-010',
                  'P00-011', 'P00-012', 'P00-013', 'P00-014', 'P00-015', 'P00-016', 'P00-017', 'P00-018', 'P00-019', 'P00-020'],
    'name': ['Smart TV 55"', 'Laptop - Core i7', 'Smartphone - X10', 'Wireless Headphones', 'Gaming Console', 'Drone - Pro',
             'Smart Watch', 'Bluetooth Speaker', 'DSLR Camera', 'Tablet - iPad Air', 'Desktop PC', 'VR Headset',
             'Home Theater System', 'Action Camera', 'Wireless Router', 'Smart Thermostat', 'E-book Reader',
             'Portable Projector', 'Fitness Tracker', 'Wireless Earbuds'],
    'price': [8500000, 15000000, 7200000, 1500000, 6000000, 12500000, 3000000, 800000, 10000000, 9500000,
              12000000, 3800000, 9000000, 2200000, 1200000, 1700000, 900000, 4500000, 750000, 1200000]
}

shipping_data = {
    'shippingID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'companyName': ['FastShip', 'SwiftDelivery', 'QuickShip', 'RapidTransit', 'ExpressShip'],
    'fee': [8000, 7000, 6000, 5500, 6500]
}

transactions_data = {
    'transactionID': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008', 'T009', 'T010',
                      'T011', 'T012', 'T013', 'T014', 'T015'],
    'transactionDate': ['2024-03-20', '2024-03-20', '2024-03-21', '2024-03-21', '2024-03-22', '2024-03-22',
                        '2024-03-23', '2024-03-23', '2024-03-24', '2024-03-24', '2024-03-25', '2024-03-25',
                        '2024-03-26', '2024-03-26', '2024-03-27'],
    'transactionStatus': ['Completed', 'Pending', 'Completed', 'Pending', 'Completed', 'Completed',
                          'Pending', 'Completed', 'Pending', 'Completed', 'Pending', 'Completed',
                          'Pending', 'Completed', 'Pending'],
    'transactionPrice': [8500000, 15000000, 7200000, 1500000, 6000000, 12500000, 3000000, 800000, 10000000,
                         9500000, 12000000, 3800000, 9000000, 2200000, 1200000],
    'customerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010',
                   'C011', 'C012', 'C013', 'C014', 'C015'],
    'shippingID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S001', 'S002', 'S003', 'S004', 'S005',
                   'S001', 'S002', 'S003', 'S004', 'S005'],
    'productID': [['P00-001'], ['P00-002'], ['P00-003'], ['P00-004'], ['P00-005'], ['P00-006'], ['P00-007'], ['P00-008'],
                  ['P00-009'], ['P00-010'], ['P00-011'], ['P00-012'], ['P00-013'], ['P00-014'], ['P00-015']]
}

# Create DataFrames
customers_df = pd.DataFrame(customers_data)
products_df = pd.DataFrame(products_data)
shipping_df = pd.DataFrame(shipping_data)
transactions_df = pd.DataFrame(transactions_data)

# App title
st.title('Customer Information Lookup')

# Input field for transaction ID
transaction_id = st.text_input('Enter Transaction ID:', '')

# Check if transaction ID is provided
if transaction_id:
    # Filter transactions DataFrame based on transaction ID
    transaction = transactions_df[transactions_df['transactionID']
                                  == transaction_id]

    if not transaction.empty:
        # Retrieve customer ID and transaction price from filtered transaction
        customer_id = transaction['customerID'].iloc[0]
        transaction_price = transaction['transactionPrice'].iloc[0]

        # Filter customers DataFrame based on customer ID
        customer = customers_df[customers_df['customerID'] == customer_id]

        # Check if customer
        if not customer.empty:
            # Display customer information
            st.write('Customer ID:', customer['customerID'].iloc[0])
            st.write('Name:', customer['name'].iloc[0])
            st.write('Address:', customer['address'].iloc[0])

            # Retrieve product IDs purchased by the customer
            product_ids = transaction['productID'].iloc[0]

            # Filter products DataFrame based on product IDs
            purchased_products = products_df[products_df['productID'].isin(
                product_ids)]

            # Display purchased items and their prices
            st.write('Items Purchased:')
            for idx, row in purchased_products.iterrows():
                st.write(f"- {row['name']}: ${row['price']}")

            # Display total amount spent by the customer
            st.write('Total Amount Spent:', f"${transaction_price}")
        else:
            st.write('Customer not found for the given transaction ID.')
    else:
        st.write('Transaction ID not found.')
