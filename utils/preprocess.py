import re
import pandas as pd

def clean_text(text):
    """
    Cleans text by removing special characters and extra spaces.
    """
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def preprocess_skills(skills_text):
    """
    Converts comma-separated skills into a list and cleans them.
    """
    skills = [clean_text(skill) for skill in skills_text.split(",")]
    return skills

def filter_jobs_by_skills(job_df, user_skills):
    """
    Filters job postings based on user skills.
    """
    job_df["matched_skills"] = job_df["required_skills"].apply(lambda x: set(preprocess_skills(x)) & set(user_skills))
    return job_df[job_df["matched_skills"].apply(len) > 0]

if __name__ == "__main__":
    sample_text = "  Python, Machine Learning, SQL! "
    print(preprocess_skills(sample_text))  # Output: ['python', 'machine learning', 'sql']