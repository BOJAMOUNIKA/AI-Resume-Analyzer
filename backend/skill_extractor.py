import pandas as pd

# Load skills dataset
skills_df = pd.read_csv("datasets/skills.csv")

# Convert skills into list
skills_list = skills_df['skill'].tolist()

def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in skills_list:

        if skill.lower() in text:
            detected_skills.append(skill)

    return list(set(detected_skills))