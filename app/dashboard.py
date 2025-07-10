import streamlit as st
import pandas as pd
import sqlite3
import os
import altair as alt

st.title("📊 Local Economic Dashboard")
st.write("Explore Data By Region (Unemployment, Population & Income)")

# Paths
db_path = "db/local_data.db"

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
        st.error(f"❌ Failed to load data: {e}")
        st.stop()

df = load_data(db_path)

# Filters
years = sorted(df["year"].unique())
states = sorted(df["state"].dropna().unique())

selected_year = st.selectbox("📆 Select Year", years, index=len(years)-1)
selected_state = st.selectbox("🇺🇸 Select State", states)

filtered = df[(df["year"] == selected_year) & (df["state"] == selected_state)]

# Metric and chart type selection
metric = st.selectbox("📈 Select Metric to Visualize", [
    "unemployment_rate",
    "population",
    "median_income"
])

metric_label = {
    "unemployment_rate": "Unemployment Rate",
    "population": "Population",
    "median_income": "Median Income"
}

chart_type = st.selectbox("📊 Select Chart Type", ["Bar", "Line", "Area"])

# Prepare data for chart: top 25 ZIP codes by selected metric
filtered_top = filtered.sort_values(metric, ascending=False).head(25)

# Build chart
base = alt.Chart(filtered_top).encode(
    x=alt.X("zip_code:N", sort='-y', title="ZIP Code"),
    y=alt.Y(f"{metric}:Q", title=metric_label[metric]),
    tooltip=["zip_code", metric]
).properties(
    width=700,
    height=400
)

if chart_type == "Bar":
    chart = base.mark_bar()
elif chart_type == "Line":
    chart = base.mark_line(point=True)
elif chart_type == "Area":
    chart = base.mark_area(opacity=0.6)
else:
    chart = base.mark_bar()

st.altair_chart(chart, use_container_width=True)

# Summary statistics
mean_val = filtered[metric].mean()
median_val = filtered[metric].median()

st.markdown(f"""
**Summary Statistics for {metric_label[metric]} ({selected_state}, {selected_year}):**

- Mean: {mean_val:,.2f}
- Median: {median_val:,.2f}
""")

# CSV Download Button
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(filtered)

st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv_data,
    file_name=f"filtered_data_{selected_state}_{selected_year}.csv",
    mime="text/csv"
)
