import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import tempfile
from fpdf import FPDF

st.set_page_config(page_title="AI Business Automator", layout="wide")

st.title("🚀 Smart Business Automation Tool")
st.markdown("Upload your messy Excel or CSV files to clean, analyze, and report in seconds.")

if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False
if "data_cleaned" not in st.session_state:
    st.session_state.data_cleaned = False
if "df" not in st.session_state:
    st.session_state.df = None

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
        df = st.session_state.df
        duplicates = df.duplicated().sum()
        df.drop_duplicates(inplace=True)

        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())

        st.session_state.df = df
        st.session_state.data_cleaned = True

        st.write(f"✔️ Removed {duplicates} duplicates")
        st.write("✔️ Fixed missing values.")
        st.dataframe(df.head(10))

if st.session_state.data_cleaned:
    df = st.session_state.df

    st.header("Step 3: Key Business Metrics")
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        m1, m2, m3 = st.columns(3)
        main_col = numeric_cols[0]

        total_val = df[main_col].sum()
        avg_val = df[main_col].mean()
        count_val = len(df)

        m1.metric(label=f"Total {main_col}", value=f"{total_val:,.2f}")
        m2.metric(label=f"Average {main_col}", value=f"{avg_val:,.2f}")
        m3.metric(label="Total Records", value=count_val)
    else:
        st.warning("No numeric columns found to calculate metrics")

    st.header("Step 4: Data Visualization")
    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    all_cols = df.columns.tolist()

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        x_axis = st.selectbox("Select X-axis (Category)", all_cols)
        if len(numeric_cols) > 0:
            y_axis = st.selectbox("Select Y-axis (Values)", numeric_cols)
            df.groupby(x_axis)[y_axis].sum().plot(kind='bar', ax=ax, color='skyblue')
            ax.set_title(f"{y_axis} by {x_axis}")
            st.pyplot(fig)
        else:
            st.error("Cannot create Bar Chart without numeric columns.")

    elif chart_type == "Line Chart":
        if len(numeric_cols) > 0:
            y_axis = st.selectbox("Select Trend Column", numeric_cols)
            ax.plot(df.index, df[y_axis], marker='o', color='green')
            ax.set_title(f"Trend of {y_axis}")
            st.pyplot(fig)
        else:
            st.error("Cannot create Line Chart without numeric columns.")

    elif chart_type == "Pie Chart":
        cat_col = st.selectbox("Select Category Column", all_cols)
        df[cat_col].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_ylabel('')
        st.pyplot(fig)

    st.divider()
    st.header("Step 5: Export Results")
    ex_col1, ex_col2 = st.columns(2)

    with ex_col1:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Cleaned Data', index=False)

        st.download_button(
            label="📥 Download Cleaned Excel",
            data=buffer.getvalue(),
            file_name="cleaned_data.xlsx",
            mime="application/vnd.ms-excel"
        )

    with ex_col2:
        if st.button("Generate PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, txt="Business Intelligence Report", ln=True, align='C')

            pdf.set_font("Arial", size=12)
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Total Records: {len(df)}", ln=True)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
                fig.savefig(tmpfile.name, format="png")
                pdf.image(tmpfile.name, x=10, y=50, w=180)

            pdf_output = pdf.output(dest='S').encode('latin-1')
            st.download_button(
                label="📩 Download PDF Report",
                data=pdf_output,
                file_name="Business_Report.pdf",
                mime="application/pdf"
            )

if uploaded_file is None:
    st.info("Please upload a file to begin.")
