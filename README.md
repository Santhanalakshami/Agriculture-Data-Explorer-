

🌾 ICRISAT Agriculture Analytics Dashboard
❤️ “If you eat today, thank a farmer.” 👨‍🌾🌱🌽

A full-stack data analytics project exploring 50+ years of Indian crop data using EDA, SQL analytics, and interactive dashboards via Streamlit and Power BI.

📌 Project Summary
Category	Description
📁 Dataset	ICRISAT District-Level Agriculture Dataset (1966 onwards)
🧪 Tools Used	Python (Pandas, Seaborn, Matplotlib), PostgreSQL, SQLAlchemy
📊 Dashboards	Built with Streamlit (Web UI) and Power BI (Business Intelligence visuals)
📈 Focus Areas	Crop yield trends, top producing states, year-wise analysis, heatmaps

🧠 Key Features
🔍 Exploratory Data Analysis (EDA)
Histograms, pie charts, and heatmaps

Crop-wise area, yield, and production over time

Top crops by state and district

🧮 SQL-Based Insights
Year-over-year trends

State/district production rankings

Yield efficiency calculations

Crop contribution % by state

💻 Interactive Dashboards
Streamlit: Real-time SQL output with filter controls

Power BI: Professionally designed reports with slicers & maps

📂 Project Structure
bash
Copy
Edit
📦 Agriculture-ICRISAT-Dashboard/
│
├── data/                 # Excel dataset (raw)
├── eda/                  # EDA notebooks with plots
├── sql/                  # PostgreSQL queries
├── streamlit_app/        # Streamlit dashboard
├── powerbi/              # Power BI .pbix file
├── requirements.txt      # Python dependencies
└── README.md             # This file
⚙️ Setup Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/agriculture-dashboard.git
cd agriculture-dashboard
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run Streamlit App
bash
Copy
Edit
cd streamlit_app
streamlit run app.py
⚠️ Note: Update your PostgreSQL connection string in app.py before running.

🖼️ Sample Visuals
Histogram (Wheat Yield)	Correlation Heatmap

Streamlit SQL Output	Power BI Crop Dashboard

📚 Dataset Details
Source: ICRISAT District-Level Data

Fields: Area, Production, Yield

Time Period: 1966 onward

Crops Covered: Rice, Wheat, Oilseeds, Sugarcane, Sunflower, and more

Regions: Indian states and districts

