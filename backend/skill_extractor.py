import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Skills dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "datasets",
    "skills.csv"
)

# Load skills dataset
skills_df = pd.read_csv(dataset_path)

skills_list = skills_df['skill'].tolist()

def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in skills_list:

        if skill.lower() in text:
            detected_skills.append(skill)

    return list(set(detected_skills))