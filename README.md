# 🌱 Agricultural Insights Dashboard – Powered by ICRISAT Data

This project delivers an interactive analytical dashboard built using **Streamlit**, **PostgreSQL**, and **Power BI**, aimed at understanding trends and performance in Indian agriculture. The data originates from the ICRISAT district-level database.

---

## 📌 Key Highlights

- 📁 CSV-based EDA Mode (via Jupyter & Streamlit)
- 🧠 SQL Query Mode with auto-visualization
- 📊 Power BI Dashboard for high-level business analysis
- 📉 Insightful charts: rice yield, oilseed trends, wheat performance, and more

---

## 📂 Folder Layout

```
.
├── eda.py                   # Streamlit app with two modes
├── eda.ipynb                # Notebook for data exploration
├── agriculture_data.sql     # Raw SQL queries used in dashboard
├── EDA.pbix, sql.pbix       # Power BI files (open with Power BI Desktop)
├── requirements.txt         # Dependencies
└── data/                    # CSV file location
```

---

## 🚀 Get Started

### 1. Install Dependencies

pip install -r requirements.txt
```

### 2. Run the Streamlit App

streamlit run eda.py
```

---

## 🔍 Features by Mode

### Mode 1: 📁 CSV Explorer
- Visualize histograms, correlations, and top producers
- Works with cleaned `.csv` data locally

### Mode 2: 📊 SQL Explorer
- Choose from 10 preloaded queries (e.g., rice trends, maize yield)
- Dynamic charts via Matplotlib and Seaborn
- Query logic stored in `agriculture_data.sql`

---

## 📈 Power BI Dashboard

To view `EDA.pbix`, open the file using [Power BI Desktop](https://powerbi.microsoft.com/). The report mirrors SQL-based insights and provides rich dashboard-level summaries.

---

## 🧠 Data Source

- ICRISAT Open Data Platform  
- District-level agricultural data on crops, area, yield, and production

---

## 🤝 Credits

Developed by **Santhanalakshmi**, with support from Streamlit, PostgreSQL, and the open ICRISAT dataset.

---

## ❤️ Acknowledgment

> “If you eat today, thank a farmer.” 👨‍🌾🌾🌽
