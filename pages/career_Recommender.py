import streamlit as st
import pandas as pd
from models.job_matching import recommend_career

def run():
    st.title("AI Career Path Recommender 🏆")
    
    skills = st.text_area("Enter your skills (comma-separated):")
    interests = st.text_input("Enter your interests:")
    experience = st.selectbox("Select your experience level", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Get Career Recommendations"):
        recommendations = recommend_career(skills, interests, experience)
        st.write("### Recommended Career Paths:")
        for rec in recommendations:
            st.success(f"🔹 {rec}")

if __name__ == "__main__":
    run()