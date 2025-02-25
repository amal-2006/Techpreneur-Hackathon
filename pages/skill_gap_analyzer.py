import streamlit as st
from models.skill_gap_analyzer import analyze_skill_gap  # Import function

def run():
    st.title("Skill Gap Analyzer")
    
    current_skills = st.text_input("Enter your current skills (comma-separated):")
    
    if st.button("Analyze"):
        if current_skills:
            current_skills_list = [skill.strip() for skill in current_skills.split(",")]
            recommendations = analyze_skill_gap(current_skills_list)
            
            st.subheader("Recommended Skills & Courses")
            for skill, courses in recommendations.items():
                st.write(f"**{skill}**: {', '.join(courses)}")
        else:
            st.warning("Please enter your skills.")

if __name__ == "__main__":
    run()