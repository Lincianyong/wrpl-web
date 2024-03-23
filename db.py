import streamlit as st

import mysql.connector
import pandas as pd

db_conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="ugm_wrpl"
)