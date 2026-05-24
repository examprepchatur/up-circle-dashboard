
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="UP Circle Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="UP Circle Dashboard",
        options=[
            "Executive Overview",
            "Mail Growth",
            "Parcel Growth",
            "Digital COD",
            "Foreign Destination",
            "DNK Portal"
        ],
        icons=[
            "house-fill",
            "envelope-fill",
            "box-fill",
            "credit-card-fill",
            "globe-central-south-asia",
            "truck"
        ],
        default_index=0
    )

st.markdown("""
<div style='background:linear-gradient(90deg,#d32f2f,#8e0000);
padding:20px;border-radius:10px;color:white;margin-bottom:20px;'>
<h2>INDIA POST — UP CIRCLE</h2>
<p>O/o Chief Postmaster General | Parcel & Mails Branch</p>
</div>
""", unsafe_allow_html=True)

st.info("Use the sidebar to navigate across KPI pages.")
