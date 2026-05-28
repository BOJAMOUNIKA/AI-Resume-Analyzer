import streamlit as st
import sys
import os

# Add backend folder to path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../backend"
        )
    )
)

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from job_recommender import recommend_jobs
from interview_generator import generate_questions
from database import save_analysis, get_all_analyses

# Streamlit page config
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

# App title
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get ATS analysis, "
    "job recommendations, and interview preparation."
)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# Process uploaded resume
if uploaded_file is not None:

    # Create temp upload directory
    upload_dir = "temp_uploads"

    os.makedirs(upload_dir, exist_ok=True)

    # Save uploaded file temporarily
    temp_path = os.path.join(
        upload_dir,
        uploaded_file.name
    )

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract resume text
    text = extract_text_from_pdf(temp_path)

    # Extract skills
    skills = extract_skills(text)

    # Target job skills
    target_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "AWS",
        "Docker",
        "Deep Learning"
    ]

    # ATS score analysis
    ats_result = calculate_ats_score(
        skills,
        target_skills
    )

    # Job recommendations
    recommendations = recommend_jobs(skills)

    # Interview questions
    questions = generate_questions(skills)

    # Save analysis in database
    recommended_roles = [
        job["role"]
        for job in recommendations
    ]

    save_analysis(
        uploaded_file.name,
        ats_result["score"],
        skills,
        recommended_roles
    )

    # ATS Score section
    st.subheader("📊 ATS Score")

    st.progress(
        int(ats_result["score"])
    )

    st.write(
        f"ATS Score: {ats_result['score']}%"
    )

    # Detected Skills section
    st.subheader("🛠 Detected Skills")

    for skill in skills:
        st.success(skill)

    # Missing Skills section
    st.subheader("❌ Missing Skills")

    for skill in ats_result["missing_skills"]:
        st.warning(skill)

    # Recommended Roles section
    st.subheader("💼 Recommended Roles")

    for job in recommendations:

        st.info(
            f"{job['role']} "
            f"({job['match']}% match)"
        )

    # Interview Questions section
    st.subheader("🎯 Interview Questions")

    for skill, ques_list in questions.items():

        st.markdown(f"### {skill}")

        for q in ques_list:
            st.write(f"• {q}")

# Analysis History section
st.subheader("📁 Previous Analyses")

history = get_all_analyses()

for record in history:

    st.write(
        f"""
📄 File: {record[1]}

🎯 ATS Score: {record[2]}%

🛠 Skills: {record[3]}

💼 Roles: {record[4]}

🕒 Time: {record[5]}
"""
    )