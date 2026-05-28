import pandas as pd
import os

# Base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "datasets",
    "interview_questions.csv"
)

# Load interview dataset
questions_df = pd.read_csv(dataset_path)

def generate_questions(resume_skills):

    interview_questions = {}

    for skill in resume_skills:

        filtered_questions = questions_df[
            questions_df['skill'].str.lower()
            == skill.lower()
        ]

        questions = filtered_questions[
            'question'
        ].tolist()

        if questions:
            interview_questions[skill] = questions

    return interview_questions