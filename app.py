import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title("CSV Analyzer")

# File upload widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Display data table
    st.subheader("Data")
    st.dataframe(df)
    
    # Display statistics
    st.subheader("Statistics")
    st.write(df.describe())
    
    # Display histogram
    st.subheader("Visualization")
    
    # Get numeric columns only
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    
    if numeric_cols:
        # Let user select column
        col = st.selectbox("Select column to visualize", numeric_cols)
        
        # Create histogram
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(df[col], bins=20, edgecolor='black')
        ax.set_title(f"Distribution of {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        
        st.pyplot(fig)
    else:
        st.write("No numeric columns found for visualization")
