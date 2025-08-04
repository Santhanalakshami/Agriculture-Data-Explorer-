import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

st.set_page_config(page_title="ICRISAT Full Dashboard", layout="wide")
st.title(":red[🌾 ICRISAT Agricultural Data Dashboard 👨‍🌾]")

mode = st.sidebar.radio("Choose Mode", ["📊 SQL Dashboard", "📁 CSV EDA Dashboard"])

if mode == "📊 SQL Dashboard":
    st.sidebar.header("🔐 Database Credentials")
    db_user = st.sidebar.text_input("Username", value="postgres")
    db_pass = st.sidebar.text_input("Password", type="password", value="Regular20")
    db_host = st.sidebar.text_input("Host", value="localhost")
    db_port = st.sidebar.text_input("Port", value="5432")
    db_name = st.sidebar.text_input("Database", value="postgres")

    @st.cache_resource
    def get_engine():
        return create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

    try:
        engine = get_engine()
    except Exception as e:
        st.error(f"❌ Database connection failed: {e}")
        st.stop()

    query_dict = {
        "1️⃣ Year-wise Trend of Rice Production (Top 3 States)": """
            WITH top_states AS (
                SELECT state_name
                FROM agriculture_data
                GROUP BY state_name 
                ORDER BY SUM(rice_production) DESC
                LIMIT 3
            )
            SELECT
                year,
                state_name,
                SUM(rice_production) AS total_rice_production
            FROM agriculture_data
            WHERE state_name IN (SELECT state_name FROM top_states)
            GROUP BY year, state_name
            ORDER BY year, total_rice_production DESC;
        """,
        "2️⃣ Top 5 Districts by Wheat Yield Increase (Last 5 Years)": """
            WITH last_five_years AS (
                SELECT DISTINCT year FROM agriculture_data ORDER BY year DESC LIMIT 5
            ),
            year_range AS (
                SELECT MAX(year) AS latest_year, MIN(year) AS earliest_year FROM last_five_years
            ),
            district_yields AS (
                SELECT dist_name, year, AVG(wheat_yield) AS avg_yield
                FROM agriculture_data 
                WHERE year IN (SELECT latest_year FROM year_range) 
                   OR year IN (SELECT earliest_year FROM year_range) 
                GROUP BY dist_name, year
            ),
            yield_comparison AS (
                SELECT dist_name,
                    MAX(CASE WHEN year = (SELECT latest_year FROM year_range) THEN avg_yield END) AS yield_now,
                    MAX(CASE WHEN year = (SELECT earliest_year FROM year_range) THEN avg_yield END) AS yield_before
                FROM district_yields
                GROUP BY dist_name
            )
            SELECT
              dist_name, yield_before, yield_now,
              yield_now - yield_before AS yield_increase
            FROM yield_comparison
            WHERE yield_now IS NOT NULL AND yield_before IS NOT NULL
            ORDER BY yield_increase DESC
            LIMIT 5;
        """,
        "3️⃣ States with Highest Oilseed Production Growth (5-Year)": """
            WITH recent_years AS (
                SELECT DISTINCT year FROM agriculture_data ORDER BY year DESC LIMIT 5
            ),
            oilseed_summary AS (
                SELECT state_name, year, SUM(oilseeds_production) AS total_production
                FROM agriculture_data
                WHERE year IN (SELECT year FROM recent_years)
                GROUP BY state_name, year
            ),
            pivoted AS (
                SELECT state_name,
                    MAX(CASE WHEN year = (SELECT MIN(year) FROM recent_years) THEN total_production END) AS production_start,
                    MAX(CASE WHEN year = (SELECT MAX(year) FROM recent_years) THEN total_production END) AS production_end
                FROM oilseed_summary
                GROUP BY state_name
            )
            SELECT
                state_name, production_start, production_end,
                ROUND((((production_end - production_start) / production_start) * 100)::numeric, 2) AS growth_rate_percent
            FROM pivoted
            WHERE production_start IS NOT NULL AND production_end IS NOT NULL AND production_start <> 0
            ORDER BY growth_rate_percent DESC
            LIMIT 5;
        """,
        "4️⃣ District-wise Correlation (Rice Production vs Area)": """
            SELECT dist_name, state_name,
            CASE
                WHEN 
                    COUNT(*) > 1 AND
                    SQRT(COUNT(*) * SUM(rice_production * rice_production) - POWER(SUM(rice_production), 2)) > 0 AND
                    SQRT(COUNT(*) * SUM(rice_area * rice_area) - POWER(SUM(rice_area), 2)) > 0
                THEN
                    (
                        (COUNT(*) * SUM(rice_production * rice_area) - SUM(rice_production) * SUM(rice_area)) /
                        (
                            SQRT(COUNT(*) * SUM(rice_production * rice_production) - POWER(SUM(rice_production), 2)) *
                            SQRT(COUNT(*) * SUM(rice_area * rice_area) - POWER(SUM(rice_area), 2))
                        )
                    )
                ELSE NULL
            END AS rice_corr
            FROM agriculture_data
            WHERE rice_production IS NOT NULL AND rice_area IS NOT NULL
            GROUP BY dist_name, state_name;
        """,
        "5️⃣ Cotton Production Trend in Top 5 States": """
            WITH total_cotton AS (
                SELECT state_name, SUM(cotton_production) AS total
                FROM agriculture_data
                GROUP BY state_name
                ORDER BY total DESC
                LIMIT 5
            ),
            cotton_trend AS (
                SELECT year, state_name, SUM(cotton_production) AS yearly_production
                FROM agriculture_data
                WHERE state_name IN (SELECT state_name FROM total_cotton)
                GROUP BY year, state_name
            )
            SELECT * FROM cotton_trend
            ORDER BY year, state_name;
        """,
        "6️⃣ Top Groundnut Producing Districts (2017)": """
            SELECT dist_name, state_name, groundnut_production
            FROM agriculture_data
            WHERE year = 2017
            ORDER BY groundnut_production DESC
            LIMIT 5;
        """,
        "7️⃣ Annual Average Maize Yield by Year": """
            SELECT year, ROUND(AVG(maize_yield)::numeric, 2) AS avg_maize_yield
            FROM agriculture_data
            GROUP BY year
            ORDER BY year;
        """,
        "8️⃣ Oilseeds Area by State": """
            SELECT state_name, ROUND(SUM(oilseeds_area)::numeric,2) AS total_oilseeds_area
            FROM agriculture_data
            GROUP BY state_name
            ORDER BY total_oilseeds_area DESC;
        """,
        "9️⃣ Districts with Highest Rice Yield": """
            SELECT dist_name, state_name, MAX(rice_yield) AS max_rice_yield
            FROM agriculture_data
            GROUP BY dist_name, state_name
            ORDER BY max_rice_yield DESC
            LIMIT 5;
        """,
        "🔟 Compare Wheat vs Rice Production (Top 5 States)": """
            WITH top_states AS (
                SELECT state_name, SUM(wheat_production + rice_production) AS total_production
                FROM agriculture_data
                GROUP BY state_name
                ORDER BY total_production DESC
                LIMIT 5
            )
            SELECT
                year, state_name,
                ROUND(SUM(wheat_production)::numeric, 2) AS total_wheat,
                ROUND(SUM(rice_production)::numeric, 2) AS total_rice
            FROM agriculture_data
            WHERE state_name IN (SELECT state_name FROM top_states)
            GROUP BY year, state_name
            ORDER BY year, state_name;
        """
    }

    selected_query = st.sidebar.selectbox("📌 Choose SQL Report", list(query_dict.keys()))
    if st.button("▶️ Run Query"):
        st.balloons()
        try:
            result_df = pd.read_sql_query(query_dict[selected_query], engine)
            st.subheader(f"Result: {selected_query}")
            st.dataframe(result_df, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Query failed: {e}")
    else:
        st.info("💡 Select a query and click 'Run Query'")

elif mode == "📁 CSV EDA Dashboard":
    uploaded_file = st.file_uploader("Upload ICRISAT CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(r"\(.*?\)", "", regex=True)
            .str.replace(" ", "_")
            .str.rstrip("_")
        )
        df.replace(-1, np.nan, inplace=True)
        df.dropna(axis=1, how="all", inplace=True)
        df.dropna(axis=0, how="all", inplace=True)
        df.fillna(df.mean(numeric_only=True), inplace=True)

        section = st.sidebar.radio("Select EDA Section", [
            "📋 Dataset Overview", 
            "📊 Histogram Visualization", 
            "🔗 Correlation Heatmap"
        ])

        if section == "📋 Dataset Overview":
            st.subheader("📋 First 5 Rows")
            st.dataframe(df.head())
            st.subheader("📟 Data Summary")
            st.write(df.describe())
            st.subheader("📉 Missing Values")
            st.write(df.isnull().sum())
            st.subheader("🧑‍💼 Duplicate Records")
            st.write(df.duplicated().sum())

        elif section == "📊 Histogram Visualization":
            st.subheader("🌱 Crop Distribution Histograms")
            crop_options = [
                "rice", "wheat", "oilseeds", "sunflower", "sugarcane", 
                "maize", "soyabean", "kharif_sorghum", "rabi_sorghum",
                "groundnut", "pearl_millet", "finger_millet"
            ]
            crop = st.selectbox("🌿 Select a Crop", crop_options)
            fig, axes = plt.subplots(1, 3, figsize=(18, 5))
            for ax, metric, color in zip(axes, ["production", "yield", "area"], ["red", "green", "blue"]):
                column_name = f"{crop}_{metric}"
                if column_name in df.columns:
                    ax.hist(df[column_name].dropna(), bins=50, color=color, edgecolor='black')
                    ax.set_title(f"{crop.capitalize()} {metric.capitalize()} Distribution")
                    ax.set_xlabel(metric.capitalize())
                    ax.set_ylabel("Frequency")
                else:
                    ax.set_visible(False)
            st.pyplot(fig)

        elif section == "🔗 Correlation Heatmap":
            st.subheader("🔗 Correlation Heatmap")
            selected_columns = [
                'year', 'rice_production', 'rice_yield',
                'wheat_production', 'wheat_yield',
                'oilseeds_production', 'oilseeds_yield',
                'sunflower_production', 'sunflower_yield',
                'sugarcane_production', 'sugarcane_yield',
                'maize_production', 'maize_yield',
                'soyabean_production', 'soyabean_yield',
                'kharif_sorghum_production', 'kharif_sorghum_yield',
                'rabi_sorghum_production', 'rabi_sorghum_yield',
                'groundnut_production', 'groundnut_yield',
                'pearl_millet_production', 'pearl_millet_yield',
                'finger_millet_production', 'finger_millet_yield'
            ]
            numeric_cols = [col for col in selected_columns if col in df.columns]
            correlation = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(16, 12))
            sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
            st.pyplot(fig)
    else:
        st.info("👈 Upload a CSV file to get started.")

 
    

#Final Touches
st.markdown("---")
# Display an image and a header
st.header(":green[ Welcome to Agriculture  Dashboard 👨‍🌾👩‍🌾🌾]")
st.image("G:\Python\.venv\HD-wallpaper-green-field-sunset-clouds-countryside-farming-agriculture-landscape-thumbnail.jpg",width=1000)

st.markdown("---")
st.title(":blue[❤️ If you eat today, thank a farmer 👨‍🌾👩‍🌾🌾🥦🍚]")
