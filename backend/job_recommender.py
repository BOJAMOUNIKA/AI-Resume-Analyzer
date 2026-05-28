import pandas as pd

# Load dataset
jobs_df = pd.read_csv("../datasets/job_roles.csv")

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

    # Sort by highest match
    recommendations = sorted(
        recommendations,
        key=lambda x: x['match'],
        reverse=True
    )

    return recommendations[:3]