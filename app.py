import streamlit as st
from PyPDF2 import PdfReader

# ------------------------
# TITLE
# ------------------------
st.title("🚀 AI Resume Analyzer")
st.markdown("Helo Mister Vinay Upload your resume and get instant skill analysis + suggestions")

# ------------------------
# INPUTS
# ------------------------
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")
job_description = st.text_area("📋 Paste Job Description Here")

# ------------------------
# MAIN LOGIC
# ------------------------
if uploaded_file is not None:

    # Step 1: Read PDF
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    # Step 2: Define skills
    skills = ["python", "sql", "machine learning", "power bi", "tableau", "deep learning", "nlp"]

    # Step 3: Find skills
    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    # Step 4: Missing skills
    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    # ------------------------
    # OUTPUT
    # ------------------------
    st.success("✅ Resume analyzed successfully!")

    # Found skills
    st.subheader("💡 Found Skills")
    for skill in found_skills:
        st.write(f"✅ {skill.title()}")

    # Missing skills
    st.subheader("⚠️ Missing Skills")
    if len(missing_skills) == 0:
        st.success("You have all key skills! 🎉")
    else:
        for skill in missing_skills:
            st.write(f"❌ {skill.title()}")

    # Suggestions
    st.subheader("📌 Suggestions")
    for skill in missing_skills:
        st.write(f"👉 Consider learning {skill.title()}")

    # ------------------------
    # MATCH SCORE (IMPORTANT FEATURE)
    # ------------------------
    if job_description:

        jd_text = job_description.lower()

        matched = 0

        for skill in skills:
            if skill in jd_text and skill in text:
                matched += 1

        total = len(skills)
        score = (matched / total) * 100

        st.subheader("📊 Match Score")
        st.write(f"Your resume matches {score:.2f}% of the job requirements")