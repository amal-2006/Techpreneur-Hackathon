import pandas as pd

def recommend_career(skills_list, interests, experience):
    careers_df = pd.read_csv("data/skills_data.csv")
    careers_df.rename(columns={"Skill": "skills"}, inplace=True)

    if "skills" not in careers_df.columns:
        raise KeyError(f"The 'skills' column is missing in the dataset. Available columns: {careers_df.columns}")

    careers_df["skills"] = careers_df["skills"].astype(str).str.lower()
    matched_careers = careers_df[careers_df["skills"].apply(lambda x: any(skill in x for skill in skills_list))]

    if matched_careers.empty:
        return pd.DataFrame({"Message": ["No matching career paths found. Try adding more skills!"]})

    return matched_careers
