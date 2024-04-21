import streamlit as st
# import streamlit as st
import mysql.connector


# Initialize connection.
# conn = st.connection('mysql', type='sql')
conn = st.connection(name='wrpl', host='localhost', port=3307, username='root', password='RINNEA098123/#', database='ecommerce', type='sql', dialect='mysql')


# Perform query.
df = conn.query('SELECT name from customers;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
