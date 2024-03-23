import os
import sys
import streamlit as st
from pathlib import Path


CURR_DIR_PATH = Path(__file__).resolve().parents[0]

sys.path.append(str(CURR_DIR_PATH.parents[0]))

st.set_page_config(
    page_title="LAMDA Store",
    page_icon="👋",
)

st.write("# LAMBDA Book Store")

st.sidebar.success("Select a page to view")

st.markdown(
    """
    Albert Cristianto Halim
    Wenka Wendira Putri Bun
    Justin Nashwan Limansubroto
"""
)
