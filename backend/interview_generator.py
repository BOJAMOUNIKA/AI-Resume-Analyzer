import pandas as pd

# Load interview dataset
questions_df = pd.read_csv(
    "../datasets/interview_questions.csv"
)

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