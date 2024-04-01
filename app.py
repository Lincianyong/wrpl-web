import streamlit as st
import pandas as pd
from gspread.exceptions import SpreadsheetNotFound
import gspread
import json

try:
    credentials = st.secrets["gcp_service_account"]
    if hasattr(credentials, "to_dict"):
        credentials = credentials.to_dict()  
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1L34DCUZ6YPs_p77gq-Awidq8nuGn-ou_W2HO5uh6qdI")
    worksheet_name = "Customers"
    worksheet = sh.worksheet(worksheet_name)
    data = worksheet.get_all_values()
    headers = data.pop(0)
    existing_data = pd.DataFrame(data, columns=headers)
    existing_data = existing_data.iloc[:, :5] 
    existing_data = existing_data.dropna(how="all")
    st.dataframe(existing_data)

except gspread.exceptions.WorksheetNotFound:
    st.write(f"Worksheet '{worksheet_name}' not found.")
except SpreadsheetNotFound:
    st.write("Spreadsheet not found. Please check the URL.")
except Exception as e:
    st.write(f"Error occurred: {e}")