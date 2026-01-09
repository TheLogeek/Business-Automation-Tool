# 🚀 AI-Powered Business Automation Tool

A professional-grade Python application designed to help businesses, educators, and vendors transform messy data into actionable insights in seconds.

Built with **Streamlit**, **Pandas**, and **AI-Logic**, this tool eliminates hours of manual data entry and cleaning.

---

## 🌟 Why This Project?
Small and Medium Enterprises (SMEs) in Nigeria often struggle with disorganized sales records, student data, and inventory lists. This tool provides a "one-click" solution to:
* **Stop Manual Cleaning:** Automatically handle duplicates and missing values.
* **Instant KPI Tracking:** See Total Sales, Averages, and Volume immediately.
* **Visual Intelligence:** Generate Bar, Line, and Pie charts to understand trends.
* **Professional Reporting:** Export results to Excel or a formal PDF report.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** [Streamlit](https://streamlit.io/) (Web Interface)
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Visualization:** [Matplotlib](https://matplotlib.org/)
* **Reporting:** [FPDF](http://pyfpdf.readthedocs.io/) & [XlsxWriter](https://xlsxwriter.readthedocs.io/)

---

## 🚀 Features & Functionality

### 1. Smart Data Ingestion
Supports both **CSV** and **Excel (.xlsx)** formats. Features a secure file uploader and a raw data previewer.

### 2. Auto-Cleaning Engine
* Detects and removes duplicate entries.
* Intelligent Imputation: Uses **Median** values for missing numbers and **Categorical Fill** for missing text to ensure data integrity.

### 3. Interactive Analytics Dashboard
* **Real-time Metrics:** Calculation of key performance indicators (KPIs) like total revenue or average scores.
* **Dynamic Charts:** Users can toggle between different chart types and select custom axes for bespoke analysis.

### 4. Professional Exporting
* **Clean Data Download:** Export the sanitized dataset back to Excel.
* **PDF Report Generation:** Captures current charts and metrics into a formatted PDF document ready for meetings or records.

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/business-automation-tool.git](https://github.com/your-username/business-automation-tool.git)
   cd business-automation-tool
   ```

2.  **Install dependencies:**

    ```bash
    pip install streamlit pandas matplotlib openpyxl xlsxwriter fpdf
    ```

3.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

---

## 💡 Use Cases

  * **Retailers:** Cleaning daily sales logs and generating monthly performance reports.
  * **Educators:** Organizing student grades and visualizing class performance averages.
  * **Freelance Data Analysts:** Using the tool as a base for rapid client data sanitization.

---

## 👤 Author

**Solomon Adenuga**

  * LinkedIn: https://www.linkedin.com/in/solomon-adenuga-6251a5316
  * X (Twitter): https://x.com/TheLogeek
  * Portfolio: https://solomonadenuga.lovable.app

---

*“Turning messy data into growth opportunities.”*