import streamlit as st
import pandas as pd

# Sample product data
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

# Sample shipping data
shipping_data = {
    'shippingID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'companyName': ['FastShip', 'SwiftDelivery', 'QuickShip', 'RapidTransit', 'ExpressShip'],
    'fee': [8000, 7000, 6000, 5500, 6500]
}

# Create DataFrames
products_df = pd.DataFrame(products_data)
shipping_df = pd.DataFrame(shipping_data)

# Initialize quantities dictionary
if 'quantities' not in st.session_state:
    st.session_state.quantities = {
        product_id: 0 for product_id in products_df['productID']}

# Page title
st.title('Online Shop - Cart Page')

# Customer details
customer_name = st.text_input("Customer Name")
customer_address = st.text_input("Customer Address")

# Function to update quantity


def update_quantity(product_id, action):
    if action == 'Add':
        st.session_state.quantities[product_id] += 1
    elif action == 'Remove' and st.session_state.quantities[product_id] > 0:
        st.session_state.quantities[product_id] -= 1


# Search box for products
search_term = st.text_input("Search Product")

# Display products
for index, row in products_df.iterrows():
    if search_term.lower() == '' or search_term.lower() in row['name'].lower():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**{row['name']}** - ${row['price']}")
        with col2:
            quantity = st.session_state.quantities[row['productID']]
            if st.button('Add', key=f'add_{row["productID"]}'):
                update_quantity(row['productID'], 'Add')
            st.write(f"Quantity: {quantity}")
            if st.button('Remove', key=f'remove_{row["productID"]}'):
                update_quantity(row['productID'], 'Remove')

# Display shipping options
st.title('Shipping Options')
shipping_option = st.selectbox(
    "Select Shipping Company", options=shipping_df['companyName'])

# Display total price before shipping
total_price_before_shipping = sum(st.session_state.quantities[product_id] * products_df.loc[products_df['productID']
                                                                                            == product_id, 'price'].iloc[0] if products_df.loc[products_df['productID'] == product_id].shape[0] > 0 else 0
                                  for product_id in st.session_state.quantities)
st.write(
    f"**Total Price (before shipping fee)**: ${total_price_before_shipping}")

# Display total price after adding shipping fee
shipping_fee = shipping_df.loc[shipping_df['companyName']
                               == shipping_option, 'fee'].iloc[0]
total_price_after_shipping = total_price_before_shipping + shipping_fee
st.write(
    f"**Total Price (including shipping fee)**: ${total_price_after_shipping}")

# Display customer details
st.write("**Customer Details**")
st.write(f"Name: {customer_name}")
st.write(f"Address: {customer_address}")

# Finalize purchase button
if st.button('Finalize Purchase'):
    # Get selected products
    selected_products = [(products_df.loc[products_df['productID'] == product_id, 'name'].iloc[0],
                         st.session_state.quantities[product_id])
                         for product_id in st.session_state.quantities
                         if st.session_state.quantities[product_id] > 0]

    # Create DataFrame for purchase details
    purchase_details_df = pd.DataFrame(
        selected_products, columns=['Product', 'Quantity'])

    # Add columns for Total Price for each product
    purchase_details_df['Total Price'] = purchase_details_df['Quantity'] * products_df.loc[
        products_df['name'].isin(purchase_details_df['Product']), 'price'].values

    # Calculate total price before shipping
    total_price_before_shipping = purchase_details_df['Total Price'].sum()

    # Display purchase details in a table
    st.write("**Purchase Details**")
    st.write(f"Customer Name: {customer_name}")
    st.write(f"Customer Address: {customer_address}")
    st.write("Products Purchased:")
    st.write(purchase_details_df)

    # Display total price before shipping
    st.write(f"Total Price (before shipping): ${total_price_before_shipping}")

    # Display shipping information
    st.write(f"Shipping Company: {shipping_option}")
    st.write(f"Shipping Fee: ${shipping_fee}")

    # Calculate total price after shipping
    total_price_after_shipping = total_price_before_shipping + shipping_fee
    st.write(
        f"Total Price (including shipping): ${total_price_after_shipping}")
