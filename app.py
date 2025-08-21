import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="Retail Customer Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Title and Description ---
st.title("📊 Retail Customer Analytics Dashboard")
st.markdown("This dashboard presents key insights from the Deloitte virtual internship project, focusing on customer segmentation and sales trends.")

# --- Load Data ---
# Use a try-except block to handle potential file errors
try:
    df = pd.read_csv('data/cleaned_dataset.csv')
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("Error: The file 'data/cleaned_dataset.csv' was not found. Please ensure the file exists in the 'data' directory.")
    st.stop()

# --- Main Dashboard ---
st.header("Key Performance Indicators")

# Create columns for KPIs
col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = int(df['revenue'].sum())
    st.metric(label="Total Revenue", value=f"${total_revenue:,}")

with col2:
    unique_customers = df['customer_id'].nunique()
    st.metric(label="Unique Customers", value=unique_customers)

with col3:
    total_transactions = len(df)
    st.metric(label="Total Transactions", value=f"{total_transactions:,}")


# --- Visualizations ---
st.header("Visual Insights")

# Create columns for charts
viz_col1, viz_col2 = st.columns(2)

with viz_col1:
    st.subheader("Revenue by Product Category")
    fig1, ax1 = plt.subplots()
    # Create a clean summary dataframe for plotting
    category_revenue = df.groupby('product_category')['revenue'].sum().sort_values(ascending=False)
    sns.barplot(x=category_revenue.values, y=category_revenue.index, ax=ax1, palette="viridis")
    ax1.set_xlabel("Total Revenue ($)")
    ax1.set_ylabel("Product Category")
    st.pyplot(fig1)

with viz_col2:
    st.subheader("Revenue by State")
    fig2, ax2 = plt.subplots()
    state_revenue = df.groupby('state')['revenue'].sum().sort_values(ascending=False)
    sns.barplot(x=state_revenue.values, y=state_revenue.index, ax=ax2, palette="plasma")
    ax2.set_xlabel("Total Revenue ($)")
    ax2.set_ylabel("State")
    st.pyplot(fig2)

# --- Data Preview ---
st.header("Data Preview")
st.dataframe(df)

st.info("Dashboard created by [Your Name]. All data is from the sample dataset provided for the project.")