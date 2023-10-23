#========================================================================================
#IMPORTING LIBRARIES
#========================================================================================

import streamlit as st
import pandas as pd

#========================================================================================
# TITLE OF THE APP
#========================================================================================
st.title("CSV Data Viewer")

#========================================================================================
# Upload the CSV file
#========================================================================================
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, low_memory=False)

    #========================================================================================
    # Get the list of column names
    #========================================================================================
    column_names = df.columns.tolist()

    #========================================================================================
    # Get the corresponding data types
    #========================================================================================
    data_types = df.dtypes.tolist()

    #========================================================================================
    # Create a dictionary to hold column names and their data types
    #========================================================================================
    columns_and_types = {}
    for name, dtype in zip(column_names, data_types):
        columns_and_types[name] = dtype

    #========================================================================================
    # Display the column names and their data types
    #========================================================================================
    st.subheader("Column Names and Data Types:")
    st.write(columns_and_types)

 # Convert the "Date (charge)" column to a date type
 # Check if the 'Date (charge)' column exists
if 'Date (charge)' in df.columns:
    # Specify the correct date format used in your data
    custom_date_format = "%Y-%m-%d"  # Update with the actual date format
    
    try:
        # Attempt to convert the 'Date (charge)' column using the custom format
        df['Date (charge)'] = pd.to_datetime(df['Date (charge)'], format=custom_date_format)
        
        st.write("Data type of 'Date (charge)' column after conversion:")
        st.write(df['Date (charge)'].dtype)
    except ValueError:
        st.write("Unable to convert 'Date (charge)' column. Invalid date format.")
else:
    st.write("Column 'Date (charge)' not found in the uploaded CSV.")

