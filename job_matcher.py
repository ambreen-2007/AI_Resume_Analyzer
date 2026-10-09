# job_matcher.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_jobs(file_path="jobs.csv"):
    """
    jobs.csv file se jobs load karta hai.
    """

    jobs = pd.read_csv(file_path)

    return jobs


def calculate_match(resume_text, job_description):
    """
    Resume aur job description ke darmiyan similarity calculate karta hai.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    match_percentage = round(similarity * 100, 2)

    return match_percentage


def match_resume_with_jobs(resume_text, jobs):
    """
    Resume ko multiple jobs ke saath compare karta hai.
    """

    results = []

    for _, job in jobs.iterrows():

        score = calculate_match(
            resume_text,
            job["description"]
        )

        results.append({
            "title": job["title"],
            "company": job["company"],
            "description": job["description"],
            "match": score
        })

    results = sorted(
        results,
        key=lambda x: x["match"],
        reverse=True
    )

    return results