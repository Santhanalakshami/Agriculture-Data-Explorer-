🌾 ICRISAT Agriculture Data Analysis Dashboard
📌 Overview
This project explores the ICRISAT District-Level Agriculture Dataset to perform comprehensive Exploratory Data Analysis (EDA) and generate insightful SQL-based analytics. The results are visualized via interactive Streamlit and Power BI dashboards.

The dataset includes information on crop area, production, and yield for major crops like rice, wheat, oilseeds, and sugarcane across Indian districts from 1966 onwards.

├── data/
│   └── ICRISAT-District Level Data.xlsx
├── eda/
│   └── eda_plots.ipynb              # Histogram, heatmap, pie charts, etc.
├── sql/
│   └── agriculture_data.sql      # PostgreSQL queries for analysis
├── streamlit_app/
│   └── eda.py                       # Streamlit dashboard code
├── powerbi/
│   └── sqlpbix ,edapbix              # Power BI dashboard file
├── requirements.txt
├── README.md

📊 Key Features
✅ EDA Highlights (Python & Pandas/Matplotlib/Seaborn)
Distribution histograms for crop yield and production

Correlation heatmaps across crop metrics

Top-N state-wise crop production visualizations

District and year-wise trends

✅ SQL Analysis (PostgreSQL)
Top producing states by crop and year

Year-over-year production trends

Yield efficiency by state

Crop contribution % by region

✅ Streamlit Dashboard
📈 Multiple pages for EDA plots and SQL query visualizations

🔍 Filtering by year, state, and crop

💾 Connected to PostgreSQL database via SQLAlchemy

🌐 Hosted with Streamlit Cloud

✅ Power BI Dashboard
📌 Visual storytelling with slicers, KPIs, and maps

🎯 Supports both EDA visuals and SQL analytics

📎 Import of PostgreSQL queries via DirectQuery

🧪 Technologies Used
Python (Pandas, Matplotlib, Seaborn)

PostgreSQL (for analytics queries)

Streamlit (interactive dashboard)

Power BI (BI visualization)

SQLAlchemy (for Python-PostgreSQL connection)

🚀 Getting Started
🔧 Requirements
Install required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the Streamlit App
bash
Copy
Edit
cd streamlit_app
streamlit run eda.py
⚠️ Make sure your PostgreSQL database is up and the connection string is correct in your app.py.

📎 Power BI Dashboard
To view the Power BI dashboard:

Open the dashboard.pbix file using Power BI Desktop.

Ensure database connection points to your local or cloud PostgreSQL server.

Refresh to see updated charts.

📷 Sample Visuals
<details> <summary>📊 Click to expand</summary>
EDA Histogram	Correlation Heatmap

Streamlit SQL Output	Power BI Crop Analysis

</details>
📁 Dataset Source
ICRISAT District Level Dataset
Provided as an .xlsx file containing crop-wise data by district and year.

Dataset License: [Include license or data terms if applicable]

❤️ Acknowledgment
“If you eat today, thank a farmer” 👨‍🌾🌾🌽

