import streamlit as st

st.set_page_config(
    page_title="UP Circle Dashboard",
    layout="wide"
)

# HEADER
st.markdown("""
<div style='background:linear-gradient(90deg,#d32f2f,#8e0000);
padding:20px;border-radius:10px;color:white;margin-bottom:20px;'>
<h1>INDIA POST — UP CIRCLE</h1>
<h4>O/o Chief Postmaster General | Parcel & Mails Branch</h4>
</div>
""", unsafe_allow_html=True)

# SIDEBAR
page = st.sidebar.radio(
    "Navigate Dashboard",
    [
        "Executive Overview",
        "Mail Growth",
        "Parcel Growth",
        "Digital COD",
        "Foreign Destination",
        "DNK Portal"
    ]
)

# PAGE 1
if page == "Executive Overview":

    st.title("Executive Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Performance", "6.35")
    col2.metric("Mail Growth", "0.00")
    col3.metric("Parcel Growth", "2.27")
    col4.metric("Digital COD", "0.74")
    col5.metric("DNK Portal", "2.67")

    st.success("Executive Dashboard Loaded Successfully")

# PAGE 2
elif page == "Mail Growth":

    st.title("KPI 1 — Mail Growth")

    st.info("Mail Growth analytics page loaded.")

    st.bar_chart([10,20,15,30,25])

# PAGE 3
elif page == "Parcel Growth":

    st.title("KPI 2 — Parcel Growth")

    st.info("Parcel Growth analytics page loaded.")

    st.bar_chart([5,15,25,10,35])

# PAGE 4
elif page == "Digital COD":

    st.title("KPI 3 — Digital COD")

    mode = st.radio(
        "Select Mode",
        ["Daily Analysis", "Weekly/Monthly Trend"]
    )

    if mode == "Daily Analysis":
        st.line_chart([10,15,20,18,25])

    else:
        st.bar_chart([50,60,70,65,80])

# PAGE 5
elif page == "Foreign Destination":

    st.title("KPI 4 — Foreign Destination")

    st.info("Foreign Destination KPI loaded.")

    st.bar_chart([12,18,10,30])

# PAGE 6
elif page == "DNK Portal":

    st.title("KPI 5 — DNK Portal")

    st.info("DNK Portal KPI loaded.")

    st.bar_chart([7,14,21,28])
