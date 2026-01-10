import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import tempfile
from fpdf import FPDF
import numpy as np

st.set_page_config(page_title="AI Business Automator", layout="wide")

st.title("🚀 Smart Business Automation Tool")
st.markdown("Upload your messy Excel or CSV files to clean, analyze, and report in seconds.")

if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False
if "data_cleaned" not in st.session_state:
    st.session_state.data_cleaned = False
if "df" not in st.session_state:
    st.session_state.df = None

def text_to_number(val):
    if not isinstance(val, str):
        return val
    words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000
    }
    parts = val.lower().split()
    total = 0
    current = 0
    for part in parts:
        if part not in words:
            return val
        scale = words[part]
        if scale == 100 or scale == 1000:
            current = max(1, current) * scale
            total += current
            current = 0
        else:
            current += scale
    return total + current

st.header("Step 1: Upload Data")
uploaded_file = st.file_uploader("Choose an Excel or CSV file", type=['csv', 'xlsx'])

if uploaded_file is not None and not st.session_state.data_loaded:
    if uploaded_file.name.endswith('.csv'):
        st.session_state.df = pd.read_csv(uploaded_file)
    else:
        st.session_state.df = pd.read_excel(uploaded_file)

    st.session_state.data_loaded = True
    st.success("✅ Data Loaded Successfully!")

if st.session_state.data_loaded:
    st.header("Step 2: Preview Data")
    st.dataframe(st.session_state.df.head(10))

    st.subheader("🧹 Data Cleaning & Validation")
    if st.button("Auto-Clean Data") and not st.session_state.data_cleaned:
        df = st.session_state.df.copy()

        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        duplicates = df.duplicated().sum()
        df.drop_duplicates(inplace=True)

        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].apply(text_to_number)
                try:
                    converted = pd.to_numeric(df[col])
                    if converted.notna().sum() > len(df) * 0.6:
                        df[col] = converted
                except:
                    pass

        for col in df.select_dtypes(include=["number"]).columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            df[col] = df[col].clip(lower, upper)

        for col in df.columns:
            if df[col].dtype == "object":
                parsed_dates = pd.to_datetime(df[col], errors="coerce")
                if parsed_dates.notna().sum() > len(df) * 0.6:
                    df[col] = parsed_dates

        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())

        st.session_state.df = df
        st.session_state.data_cleaned = True

        st.write(f"✔️ Removed {duplicates} duplicates")
        st.write("✔️ Fixed missing values, outliers, data types, and formatting")
        st.dataframe(df.head(10))

if st.session_state.data_cleaned:
    df = st.session_state.df

    st.header("Step 3: Key Business Metrics")
    numeric_cols = df.select_dtypes(include=["number"]).columns

    if len(numeric_cols) > 0:
        m1, m2, m3 = st.columns(3)
        main_col = numeric_cols[0]

        m1.metric(f"Total {main_col}", f"{df[main_col].sum():,.2f}")
        m2.metric(f"Average {main_col}", f"{df[main_col].mean():,.2f}")
        m3.metric("Total Records", len(df))
    else:
        st.warning("No numeric columns found")

    st.header("Step 4: Data Visualization")
    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    all_cols = df.columns.tolist()

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        x = st.selectbox("Select X-axis", all_cols)
        y = st.selectbox("Select Y-axis", numeric_cols)
        df.groupby(x)[y].sum().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        y = st.selectbox("Select Trend Column", numeric_cols)
        ax.plot(df.index, df[y])
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        cat = st.selectbox("Select Category Column", all_cols)
        df[cat].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    st.divider()
    st.header("Step 5: Export Results")
    ex1, ex2 = st.columns(2)

    with ex1:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        st.download_button("📥 Download Cleaned Excel", buffer.getvalue(), "cleaned_data.xlsx")

    with ex2:
        if st.button("Generate PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(200, 10, "Business Intelligence Report", ln=True, align="C")
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, f"Total Records: {len(df)}", ln=True)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                fig.savefig(tmp.name)
                pdf.image(tmp.name, x=10, y=40, w=180)

            st.download_button(
                "📩 Download PDF Report",
                pdf.output(dest="S").encode("latin-1"),
                "Business_Report.pdf",
                mime="application/pdf"
            )

if uploaded_file is None:
    st.info("Please upload a file to begin.")
