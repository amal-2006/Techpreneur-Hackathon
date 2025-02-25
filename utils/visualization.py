import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_top_skills(skill_counts):
    """
    Plots the top in-demand skills using a bar chart.
    """
    fig, ax = plt.subplots()
    skill_counts.head(10).plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
    ax.set_title("Top In-Demand Skills")
    ax.set_xlabel("Skills")
    ax.set_ylabel("Job Postings Count")
    st.pyplot(fig)

def plot_salary_distribution(job_data):
    """
    Plots a salary distribution chart.
    """
    job_data["min_salary"] = job_data["salary_range"].apply(lambda x: int(x.split("-")[0].strip("$").replace(",", "")))
    
    fig, ax = plt.subplots()
    job_data["min_salary"].hist(bins=10, edgecolor="black", color="orange")
    ax.set_title("Salary Distribution")
    ax.set_xlabel("Salary ($)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

if __name__ == "__main__":
    sample_data = pd.DataFrame({"skills": ["Python", "Machine Learning", "SQL"], "counts": [150, 120, 90]})
    plot_top_skills(sample_data.set_index("skills")["counts"])