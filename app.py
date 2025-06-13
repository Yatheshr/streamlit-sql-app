import streamlit as st
import pyodbc
import pandas as pd

# Streamlit App Title
st.title("SQL Server Data Viewer")

# Read SQL Server credentials from Streamlit secrets
server = st.secrets["sqlserver"]["server"]
database = st.secrets["sqlserver"]["database"]
username = st.secrets["sqlserver"]["username"]
password = st.secrets["sqlserver"]["password"]
driver = '{ODBC Driver 17 for SQL Server}'
# Connect to SQL Server
try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    st.success("✅ Connected to SQL Server")
except Exception as e:
    st.error(f"❌ Connection failed: {e}")
    st.stop()

# Input SQL query from user
st.subheader("Run a Custom SQL Query")
query = st.text_area("Enter your SQL query", height=100)

if st.button("Run Query"):
    try:
        df = pd.read_sql(query, conn)
        st.write("### Query Results:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error executing query: {e}")
