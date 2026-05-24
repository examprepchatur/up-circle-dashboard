
import streamlit as st
import plotly.express as px
from utils.data_loader import DataLoader

loader = DataLoader()

st.title("Page 2 — KPI 1: Mail Growth")

try:
    df = loader.mail_growth()

    region_col = df.columns[0]

    regions = ["ALL"] + list(df[region_col].dropna().unique())

    region = st.selectbox("Select Region", regions)

    if region != "ALL":
        filtered = df[df[region_col] == region]
    else:
        filtered = df

    fig = px.bar(filtered, x=filtered.columns[1], y=filtered.columns[-2],
                 color=filtered.columns[-2],
                 title="Mail Growth Analysis")

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(filtered, use_container_width=True)

except Exception as e:
    st.error(e)
