import streamlit as st

import mysql.connector
import pandas as pd

db_conn = mysql.connector.connect(
    host="localhost", port=3306, user="root", password="", database="ecommerce"
)
