from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from job_recommender import recommend_jobs
from interview_generator import generate_questions

resume_path = "uploads/sample2_resume.pdf"

# Extract resume text
text = extract_text_from_pdf(resume_path)

# Extract skills
resume_skills = extract_skills(text)

print("\n===== DETECTED SKILLS =====\n")
print(resume_skills)

# ATS scoring
target_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "AWS",
    "Docker",
    "Deep Learning"
]

ats_result = calculate_ats_score(
    resume_skills,
    target_skills
)

print("\n===== ATS ANALYSIS =====\n")

print(f"ATS Score: {ats_result['score']}%")

print("\nMatched Skills:")
print(ats_result['matched_skills'])

print("\nMissing Skills:")
print(ats_result['missing_skills'])

# Job recommendations
recommendations = recommend_jobs(resume_skills)

print("\n===== RECOMMENDED JOB ROLES =====\n")

for idx, job in enumerate(
    recommendations,
    start=1
):
    print(
        f"{idx}. {job['role']} "
        f"({job['match']}% match)"
    )

# Interview questions
questions = generate_questions(
    resume_skills
)

print("\n===== INTERVIEW QUESTIONS =====\n")

for skill, ques_list in questions.items():

    print(f"\nSkill: {skill}")

    for idx, q in enumerate(
        ques_list,
        start=1
    ):
        print(f"{idx}. {q}")