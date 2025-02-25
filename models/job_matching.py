import pandas as pd

def recommend_career(skills, interests, experience):
    skills_list = [s.strip().lower() for s in skills.split(",")]
    careers_df = pd.read_csv("data/skills_data.csv")

    recommendations = careers_df[careers_df["skills"].apply(lambda x: any(skill in x.lower() for skill in skills_list))]
    
    return recommendations["career"].tolist()[:5]
