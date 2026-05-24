import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="UP Circle Dashboard", layout="wide")

EXCEL_FILE = "uploads/latest_master_file.xlsx"

# =========================
# LOAD EXCEL
# =========================

@st.cache_data

def load_sheet(sheet_name):
    return pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)

# =========================
# DOWNLOAD FUNCTION
# =========================

def download_excel(df, filename):
    output = BytesIO()

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

    st.download_button(
        label="📥 Download Excel",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.ms-excel"
    )

# =========================
# HEADER
# =========================

st.markdown("""
<div style='background:linear-gradient(90deg,#d32f2f,#8e0000);
padding:20px;border-radius:10px;color:white;margin-bottom:20px;'>
<h1>INDIA POST — UP CIRCLE</h1>
<h4>O/o Chief Postmaster General | Parcel & Mails Branch</h4>
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

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

# =====================================================
# PAGE 1 — EXECUTIVE OVERVIEW
# =====================================================

if page == "Executive Overview":

    st.title("Page 1 — Circle Executive Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Performance", "6.35")
    col2.metric("Mail Growth", "0.00")
    col3.metric("Parcel Growth", "2.27")
    col4.metric("Digital COD", "0.74")
    col5.metric("DNK Portal", "2.67")

    try:
        df = load_sheet("Total Score")

        st.subheader("Regional Score Analysis")

        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) > 0:
            fig = px.bar(
                df,
                x=df.columns[0],
                y=numeric_cols[-1],
                title="Regional Performance"
            )

            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Master Raw Data")

        st.dataframe(df, use_container_width=True)

        download_excel(df, "Executive_Overview.xlsx")

    except Exception as e:
        st.error(f"Error loading sheet: {e}")

# =====================================================
# PAGE 2 — MAIL GROWTH
# =====================================================

elif page == "Mail Growth":

    st.title("Page 2 — KPI 1: Mail Growth")

    try:
        df = load_sheet("% growth in mail traffic")

        st.subheader("Mail Growth Analytics")

        st.write("### Raw Data Preview")
        st.dataframe(df.head(20), use_container_width=True)

        region_column = df.columns[0]

        regions = ["ALL"] + list(df[region_column].dropna().unique())

        selected_region = st.selectbox(
            "Select Region",
            regions
        )

        if selected_region != "ALL":
            filtered_df = df[df[region_column] == selected_region]
        else:
            filtered_df = df

        st.subheader("Filtered Region Data")

        st.dataframe(filtered_df, use_container_width=True)

        numeric_cols = filtered_df.select_dtypes(include='number').columns

        if len(numeric_cols) >= 1:

            fig = px.bar(
                filtered_df,
                x=filtered_df.columns[1],
                y=numeric_cols[-1],
                title="Mail Growth KPI Analysis",
                color=numeric_cols[-1]
            )

            st.plotly_chart(fig, use_container_width=True)

        download_excel(filtered_df, "Mail_Growth_Data.xlsx")

    except Exception as e:
        st.error(f"Error loading Mail Growth data: {e}")

# =====================================================
# PAGE 3 — PARCEL GROWTH
# =====================================================

elif page == "Parcel Growth":

    st.title("Page 3 — KPI 2: Parcel Growth")

    try:
        df = load_sheet("% growth in Parcel traffic")

        st.dataframe(df, use_container_width=True)

        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) >= 1:

            fig = px.bar(
                df,
                x=df.columns[0],
                y=numeric_cols[-1],
                title="Parcel Growth Analysis",
                color=numeric_cols[-1]
            )

            st.plotly_chart(fig, use_container_width=True)

        download_excel(df, "Parcel_Growth.xlsx")

    except Exception as e:
        st.error(f"Error loading Parcel Growth data: {e}")

# =====================================================
# PAGE 4 — DIGITAL COD
# =====================================================

elif page == "Digital COD":

    st.title("Page 4 — KPI 3: Digital COD")

    mode = st.radio(
        "Select Analysis Mode",
        ["Daily Analysis", "Weekly/Monthly Trend"]
    )

    try:

        if mode == "Daily Analysis":

            df = load_sheet("Digital COD Transactions  (Daily position)")

        else:

            df = load_sheet("% Digital Transactions for CoD Parcels (for which payment through Digital Mode) (6)")

        st.dataframe(df, use_container_width=True)

        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) >= 1:

            fig = px.line(
                df,
                x=df.columns[0],
                y=numeric_cols[-1],
                title="Digital COD Analysis"
            )

            st.plotly_chart(fig, use_container_width=True)

        download_excel(df, "Digital_COD.xlsx")

    except Exception as e:
        st.error(f"Error loading Digital COD data: {e}")

# =====================================================
# PAGE 5 — FOREIGN DESTINATION
# =====================================================

elif page == "Foreign Destination":

    st.title("Page 5 — KPI 4: Foreign Destination")

    try:
        df = load_sheet("Foreign Destination Shipments")

        st.dataframe(df, use_container_width=True)

        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) >= 1:

            fig = px.pie(
                df,
                names=df.columns[0],
                values=numeric_cols[-1],
                title="Foreign Destination Contribution"
            )

            st.plotly_chart(fig, use_container_width=True)

        download_excel(df, "Foreign_Destination.xlsx")

    except Exception as e:
        st.error(f"Error loading Foreign Destination data: {e}")

# =====================================================
# PAGE 6 — DNK PORTAL
# =====================================================

elif page == "DNK Portal":

    st.title("Page 6 — KPI 5: DNK Portal")

    try:
        df = load_sheet("DNK Portal Shipments")

        st.dataframe(df, use_container_width=True)

        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) >= 1:

            fig = px.bar(
                df,
                x=df.columns[0],
                y=numeric_cols[-1],
                title="DNK Portal KPI Analysis",
                color=numeric_cols[-1]
            )

            st.plotly_chart(fig, use_container_width=True)

        download_excel(df, "DNK_Portal.xlsx")

    except Exception as e:
        st.error(f"Error loading DNK Portal data: {e}")
