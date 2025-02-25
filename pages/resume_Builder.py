import streamlit as st
from models.resume_parser import analyze_resume

def run():
    st.title("Smart Resume Builder 📄")

    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    if uploaded_file is not None:
        feedback = analyze_resume(uploaded_file)
        st.write("### Resume Analysis Feedback:")
        st.info(feedback)

if __name__ == "__main__":
    run()