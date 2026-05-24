
import streamlit as st
import plotly.express as px
from utils.data_loader import DataLoader

loader = DataLoader()

st.title("Page 1 — Circle Executive Overview")

try:
    df = loader.total_score()

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Total Perf. Index","6.35")
    c2.metric("Mails Growth","0.00")
    c3.metric("Parcel Growth","2.27")
    c4.metric("Digital COD","0.74")
    c5.metric("DNK Portal","2.67")

    fig = px.bar(df, x=df.columns[0], y=df.columns[-1], title="Regional Performance")
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(e)
