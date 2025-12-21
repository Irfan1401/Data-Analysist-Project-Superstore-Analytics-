import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Superstore Analytics", layout="wide")

st.title("📊 Superstore Sales & Customer Insights")
st.markdown("Dashboard ini menganalisis performa penjualan dan segmentasi pelanggan.")

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('data/sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data tidak ditemukan! Jalankan 'generate_data.py' dulu.")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
city = st.sidebar.multiselect("Pilih Kota:", options=df['City'].unique(), default=df['City'].unique())
payment = st.sidebar.multiselect("Metode Bayar:", options=df['Payment'].unique(), default=df['Payment'].unique())

df_selection = df.query("City == @city & Payment == @payment")

# --- KPI METRICS (Baris Atas) ---
total_sales = df_selection['Total Sales'].sum()
total_orders = df_selection['Order ID'].nunique()
avg_order = df_selection['Total Sales'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"Rp {total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders}")
col3.metric("Avg Order Value", f"Rp {avg_order:,.0f}")

st.markdown("---")

# --- CHARTS AREA ---
col_left, col_right = st.columns(2)

# Chart 1: Tren Penjualan Bulanan
with col_left:
    st.subheader("Tren Penjualan Bulanan")
    monthly_sales = df_selection.set_index('Date').resample('M')['Total Sales'].sum().reset_index()
    fig_line = px.line(monthly_sales, x='Date', y='Total Sales', markers=True, template="plotly_white")
    st.plotly_chart(fig_line, use_container_width=True)

# Chart 2: Penjualan per Produk
with col_right:
    st.subheader("Produk Terlaris (Revenue)")
    prod_sales = df_selection.groupby('Product')['Total Sales'].sum().sort_values(ascending=True).reset_index()
    fig_bar = px.bar(prod_sales, x='Total Sales', y='Product', orientation='h', template="plotly_white", color='Total Sales')
    st.plotly_chart(fig_bar, use_container_width=True)

# --- RFM ANALYSIS (Business Logic) ---
st.markdown("---")
st.subheader("👥 Customer Segmentation (RFM Analysis)")
st.write("Analisis ini mengelompokkan pelanggan berdasarkan kebiasaan belanja mereka.")

# Hitung RFM
snapshot_date = df['Date'].max() + pd.Timedelta(days=1)
rfm = df_selection.groupby('Customer ID').agg({
    'Date': lambda x: (snapshot_date - x.max()).days, # Recency
    'Order ID': 'count', # Frequency
    'Total Sales': 'sum' # Monetary
}).rename(columns={'Date': 'Recency', 'Order ID': 'Frequency', 'Total Sales': 'Monetary'})

# Labeling Sederhana
def segment_customer(row):
    if row['Monetary'] > 15000000 and row['Frequency'] > 5:
        return 'VIP / Loyal'
    elif row['Recency'] > 100:
        return 'At Risk (Lama tidak belanja)'
    elif row['Monetary'] < 5000000:
        return 'Low Spender'
    else:
        return 'Regular Customer'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Tampilkan Chart RFM
col_rfm1, col_rfm2 = st.columns([2, 1])

with col_rfm1:
    fig_scatter = px.scatter(rfm, x='Recency', y='Monetary', color='Segment', 
                             size='Frequency', hover_data=['Frequency'],
                             title="Customer Segments Matrix", template="plotly_white")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_rfm2:
    st.write("### Data Sampel RFM")
    st.dataframe(rfm.head(10))