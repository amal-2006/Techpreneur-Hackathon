import streamlit as st

st.set_page_config(page_title="AI Career Path Recommender", layout="wide")

st.title("Welcome to AI Career Path Recommender 🎯")

st.sidebar.header("Navigation")
st.sidebar.write("Use the left sidebar to navigate to different sections of the application.")

st.write("### Features")
st.write("""
- 🏆 **AI Career Recommender**: Get personalized career suggestions.
- 📄 **Smart Resume Builder**: Upload your resume & get ATS-friendly feedback.
- 📊 **Job Market Analyzer**: Discover top in-demand skills.
- 🔍 **Skill Gap Analyzer**: Identify missing skills & recommended courses.
""")

st.success("Go to the **sidebar** and select a page to begin!")