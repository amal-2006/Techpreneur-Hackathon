import streamlit as st
from models.job_matching import recommend_career

def run():
    st.title("Career Recommender")

    # User Inputs
    skills = st.text_input("Enter your skills (comma-separated):")
    interests = st.text_input("Enter your interests:")
    experience = st.number_input("Years of Experience:", min_value=0, step=1)

    if st.button("Recommend Career Paths"):
        skills_list = [s.strip().lower() for s in skills.split(",")] if skills else []
        recommendations = recommend_career(skills_list, interests, experience)

        if "Message" in recommendations.columns:
            st.warning(recommendations["Message"].iloc[0])  # Display no match message
        else:
            st.write("### Recommended Career Paths:")
            st.dataframe(recommendations)  # Display valid results

run()
