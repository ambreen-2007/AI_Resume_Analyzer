import streamlit as st
import pandas as pd

from resume_analyzer import analyze_resume
from skills import extract_skills
from job_matcher import load_jobs, match_resume_with_jobs


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI Resume Analyzer & Job Matching")

st.write(
    "Upload your resume and discover your skills, "
    "resume information, and best matching jobs."
)


# Sidebar
st.sidebar.header("About")

st.sidebar.write(
    "This project analyzes a PDF resume and compares "
    "it with available job descriptions using "
    "TF-IDF and Cosine Similarity."
)


# Resume upload
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    # Analyze resume
    resume_text = analyze_resume(uploaded_file)

    # Check if text was extracted
    if not resume_text.strip():

        st.error(
            "Could not extract text from this PDF. "
            "Please upload a text-based PDF resume."
        )

    else:

        # Extract skills
        found_skills = extract_skills(resume_text)

        # Resume Analysis section
        st.header("🔍 Resume Analysis")

        st.write(
            f"Resume contains approximately "
            f"**{len(resume_text.split())} words**."
        )


        # Skills section
        st.subheader("🛠️ Skills Found")

        if found_skills:

            cols = st.columns(3)

            for index, skill in enumerate(found_skills):

                cols[index % 3].success(skill)

        else:

            st.warning(
                "No skills from our current skill list were detected."
            )


        # Load jobs
        try:

            jobs = load_jobs("jobs.csv")

            # Match resume with jobs
            results = match_resume_with_jobs(
                resume_text,
                jobs
            )


            # Job matching section
            st.header("💼 Job Matching")

            st.write(
                "Jobs are ranked according to their similarity "
                "with your resume."
            )


            # Display results
            for index, result in enumerate(results):

                with st.container():

                    st.subheader(
                        f"{index + 1}. {result['title']}"
                    )

                    st.write(
                        f"**Company:** {result['company']}"
                    )

                    st.metric(
                        "Match Score",
                        f"{result['match']}%"
                    )

                    st.write(
                        result["description"]
                    )

                    st.divider()


        except Exception as error:

            st.error(
                f"Could not load job data: {error}"
            )


else:

    st.info(
        "👆 Please upload a PDF resume to start the analysis."
    )