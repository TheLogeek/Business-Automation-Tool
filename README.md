# 🚀 AI-Powered Business Automation Tool

[Use the Live App](https://Business-Automation-Tool.streamlit.app)

A professional-grade Python application designed to help businesses, educators, and vendors transform messy data into clean, analysis-ready datasets and actionable insights in seconds.

Built with **Streamlit**, **Pandas**, and advanced data-processing logic, this tool automates real-world data cleaning tasks that typically require hours of manual effort.

---

## 🌟 Why This Project?

Small and Medium Enterprises (SMEs) in Nigeria often struggle with disorganized sales records, staff data, student results, and inventory files coming from multiple sources.

This project demonstrates how automation can solve these challenges by providing a **one-click data cleaning and analysis workflow** that turns raw spreadsheets into reliable business intelligence.

Key goals:
- Eliminate repetitive manual cleaning
- Standardize inconsistent datasets
- Enable instant analysis and reporting
- Showcase real-world data engineering skills

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** [Streamlit](https://streamlit.io/) (Web Interface)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Visualization:** [Matplotlib](https://matplotlib.org/)
- **Reporting:** [FPDF](http://pyfpdf.readthedocs.io/) & [XlsxWriter](https://xlsxwriter.readthedocs.io/)

---

## 🚀 Features & Functionality

### 1. Smart Data Ingestion
- Supports **CSV** and **Excel (.xlsx)** files
- Secure file upload
- Instant raw data preview before processing

---

### 2. Advanced Auto-Cleaning Engine
Automatically prepares messy datasets for analysis by performing:

- **Duplicate Detection & Removal**
  - Identifies and removes exact duplicate rows

- **Missing Value Handling**
  - Numeric columns filled using **median imputation**
  - Categorical/text columns filled with consistent placeholders

- **Column Name Normalization**
  - Trims whitespace
  - Converts to lowercase
  - Replaces spaces with underscores for consistency

- **Global Whitespace Cleanup**
  - Removes hidden spaces from text fields that often break analysis

- **Automatic Data Type Correction**
  - Converts numeric columns stored as text into proper numeric types
  - Safely ignores columns that should remain categorical

- **Date Parsing & Standardization**
  - Detects date columns automatically
  - Converts mixed date formats into a unified datetime format

- **Outlier Handling**
  - Identifies extreme numeric values using the IQR method
  - Clips outliers to reduce distortion in metrics and charts

The result is a **clean, structured, and analysis-ready dataset** without user-written rules.

---

### 3. Interactive Analytics Dashboard
- **Real-Time KPIs**
  - Automatic calculation of totals, averages, and record counts
- **Dynamic Visualizations**
  - Bar Charts, Line Charts, and Pie Charts
  - User-selectable axes and categories
- Designed for non-technical users to explore data intuitively

---

### 4. Professional Reporting & Export
- **Excel Export**
  - Download the fully cleaned dataset for reuse or archival
- **PDF Report Generation**
  - Generates a formal business report
  - Includes key metrics and visualizations
  - Suitable for presentations, audits, or client delivery

---

## 📸 Screenshots

![Screenshot 1](screenshots/screenshot1)
![Screenshot 2](screenshots/screenshot2)
![Screenshot 3](screenshots/screenshot3)
![Screenshot 4](screenshots/screenshot4)
![Screenshot 5](screenshots/screenshot5)
![Screenshot 6](screenshots/screenshot6)

---

## 📦 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/TheLogeek/Business-Automation-Tool.git
cd Business-Automation-Tool
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