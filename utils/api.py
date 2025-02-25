import requests
import streamlit as st

def fetch_job_listings(query, location="Remote", num_results=5):
    """
    Fetches job listings from an external API.
    For now, this is a mock function (you can integrate real APIs).
    """
    job_data = [
        {"title": "AI Engineer", "company": "Google", "location": "San Francisco"},
        {"title": "Software Developer", "company": "Microsoft", "location": "Remote"},
        {"title": "Cybersecurity Specialist", "company": "IBM", "location": "New York"},
    ]
    
    return job_data[:num_results]

def fetch_course_recommendations(skill):
    """
    Fetches recommended courses based on a given skill.
    """
    course_data = {
        "Python": ["Coursera: Python for Data Science", "Udemy: Python Bootcamp"],
        "Machine Learning": ["Deep Learning Specialization", "Fast.ai ML Course"],
        "Cybersecurity": ["TryHackMe: Cybersecurity Path", "Certified Ethical Hacker Course"]
    }

    return course_data.get(skill, ["No recommendations available"])

if __name__ == "__main__":
    st.write(fetch_job_listings("AI Engineer"))