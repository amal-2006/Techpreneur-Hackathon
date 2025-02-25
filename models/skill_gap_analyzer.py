import pandas as pd

# Sample industry skills dataset
industry_skills_data = {
    "skills": ["Python", "Data Science", "Machine Learning", "Deep Learning", "Tableau"],
    "courses": [
        ["Python for Beginners", "Advanced Python"],
        ["Intro to Data Science", "Data Science Bootcamp"],
        ["Machine Learning A-Z", "Practical ML"],
        ["Deep Learning Specialization", "Neural Networks"],
        ["Tableau for Data Visualization", "Advanced Tableau"]
    ]
}
industry_skills_df = pd.DataFrame(industry_skills_data)

def analyze_skill_gap(current_skills):
    """Returns recommended courses for missing industry skills"""
    missing_skills = industry_skills_df[~industry_skills_df["skills"].isin(current_skills)]
    recommendations = {row["skills"]: row["courses"] for _, row in missing_skills.iterrows()}
    return recommendations
