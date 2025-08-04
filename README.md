🌱 Agricultural Insights Dashboard – Powered by ICRISAT Data
This project delivers an interactive analytical dashboard built using Streamlit, PostgreSQL, and Power BI, aimed at understanding trends and performance in Indian agriculture. The data originates from the ICRISAT district-level database.


📌 Key Highlights
📁 CSV-based EDA Mode (via Jupyter & Streamlit)
🧠 SQL Query Mode with auto-visualization
📊 Power BI Dashboard for high-level business analysis
📉 Insightful charts: rice yield, oilseed trends, wheat performance, and more
📂 Folder Layout
├── dashboard.py # Streamlit app with two modes
├── eda.ipynb # Notebook for data exploration
├── agriculture_data.sql # Raw SQL queries used in dashboard
├── EDA.pbix,sql.pbix # Power BI file (open with Power BI Desktop)
├── requirements.txt # Dependencies
└── data/ # CSV file location 

🚀 Get Started
1. Clone the Repo
```bash
git clone https://github.com/your-username/agriviz.git
cd agriviz

pip install -r requirements.txt

streamlit run eda.py

🔍 Features by Mode
Mode 1: 📁 CSV Explorer
Visualize histograms, correlations, top producers
Works with cleaned .csv data locally
Mode 2: 📊 SQL Explorer
Choose from 10 preloaded queries (e.g., rice trends, maize yield)
Dynamic charts via Matplot,Seaborn
Query logic stored in eda.sql
📈 Power BI Dashboard
To view EDA.pbix, use Power BI Desktop. It mirrors the SQL-based insights and offers dashboard-level summaries.

🧠 Data Source
ICRISAT Open Data Platform
District-level agricultural data (crops, area, yield, production)
🤝 Credits
Developed by Santhanalakshmi, with support from Streamlit, PostgreSQL, and the open ICRISAT dataset.

❤️ Acknowledgment
“If you eat today, thank a farmer” 👨‍🌾🌾🌽
