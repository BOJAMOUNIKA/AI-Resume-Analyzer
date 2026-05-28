import pandas as pd
import os

# Get absolute path
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "datasets",
    "job_roles.csv"
)

# Load dataset
jobs_df = pd.read_csv(dataset_path)

def recommend_jobs(resume_skills):

    recommendations = []

    for _, row in jobs_df.iterrows():

        role = row['role']

        required_skills = [
            skill.strip()
            for skill in row['skills'].split(',')
        ]

        matched_skills = 0

        for skill in required_skills:

            if skill.lower() in [
                s.lower() for s in resume_skills
            ]:
                matched_skills += 1

        match_percentage = (
            matched_skills / len(required_skills)
        ) * 100

        recommendations.append({
            "role": role,
            "match": round(match_percentage, 2)
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x['match'],
        reverse=True
    )

    return recommendations[:3]