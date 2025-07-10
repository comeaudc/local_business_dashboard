import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
import os

# Created title
st.title("📊 Local Economic Dashboard")
st.write("Explore Data By Region (Unemployment & Census)")

# Paths
db_path = "db/local_data.db"


# Load Data
@st.cache_data
def load_data(db_path):
    if not os.path.exists(db_path):
            st.error(f"Missing DB Path: {db_path}")
            st.stop()
    try:
        with sqlite3.connect(db_path) as conn:
            query = "SELECT * FROM unemployment_zip_joined"
            df = pd.read_sql(query, conn)
            return df

    except Exception as e:
        st.error("❌ Failed to load data: {e}")
        st.stop()

    query = """
        SELECT *
        FROM unemployment_zip_joined
    """
    return pd.read_sql(query, conn)

df = load_data(db_path)

# Filters

years = sorted(df["year"].unique())
states = sorted(df["state"].dropna().unique())

selected_year = st.selectbox("📆 Select Year", years, index=len(years)-1)
selected_state = st.selectbox("🇺🇸 Select State", states)

# Apply filters
filtered = df[(df["year"] == selected_year) & (df["state"] == selected_state)]

# Show table
st.subheader("📋 Filtered Data")
st.dataframe(filtered)

# Show chart
st.subheader("📈 Unemployment Rate by ZIP")
filtered_top = filtered.sort_values("unemployment_rate", ascending=False).head(20)

st.subheader("📈 Top 20 ZIP Codes by Unemployment Rate")

filtered_top = filtered.sort_values("unemployment_rate", ascending=False).head(25)

# Chart Type Selector
chart_type = st.selectbox("📊 Select Chart Type", ["Bar", "Line", "Area"])

# Base chart logic
base = alt.Chart(filtered_top).encode(
    x=alt.X("zip_code:N", sort='-y', title="ZIP Code"),
    y=alt.Y("unemployment_rate:Q", title="Unemployment Rate"),
    tooltip=["zip_code", "unemployment_rate"]
).properties(
    width=700,
    height=400
)

# Create chart based on selection
if chart_type == "Bar":
    chart = base.mark_bar()
elif chart_type == "Line":
    chart = base.mark_line(point=True)
elif chart_type == "Area":
    chart = base.mark_area(opacity=0.6)
else:
    chart = base.mark_bar()  # fallback

# Show chart
st.altair_chart(chart, use_container_width=True)