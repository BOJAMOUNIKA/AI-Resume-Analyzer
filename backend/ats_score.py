def calculate_ats_score(resume_skills, target_skills):

    matched_skills = []
    missing_skills = []

    for skill in target_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    # Calculate ATS score
    score = (len(matched_skills) / len(target_skills)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }