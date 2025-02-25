import streamlit as st
import pandas as pd

def run():
    st.title(" Real-Time Job Market Analyzer 📊")

    # Load job data
    try:
        job_data = pd.read_csv("data/job_postings.csv")
        st.write("Job data loaded successfully! ✅")
    except FileNotFoundError:
        st.error("❌ Error: job_postings.csv not found!")
        return

    # Check if required column exists
    if "required_skills" not in job_data.columns:
        st.error("❌ Error: 'required_skills' column is missing in the CSV file!")
        st.write("Available columns:", list(job_data.columns))
        return

    # Process and visualize top in-demand skills
    in_demand_skills = job_data["required_skills"].str.split(", ").explode().value_counts().head(10)
    st.write("### Top In-Demand Skills")
    st.bar_chart(in_demand_skills)

if __name__ == "__main__":
    run()
