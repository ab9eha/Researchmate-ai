import streamlit as st

from utils.pdf_processor import extract_text_from_pdf
from utils.summarizer import generate_summary
from utils.keyword_extractor import extract_keywords
from utils.quiz_generator import generate_quiz
from utils.paper_analyzer import (
    extract_objective,
    extract_limitations,
    paper_statistics
)
from utils.visualization import keyword_chart

st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchMate AI")
st.subheader("Advanced Research Paper Analyzer")

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Analyzing paper..."):

        text = extract_text_from_pdf(uploaded_file)

        summary = generate_summary(text)

        keywords = extract_keywords(text)

        objective = extract_objective(text)

        limitations = extract_limitations(text)

        stats = paper_statistics(text)

        quiz = generate_quiz(text)

    st.success("Analysis Complete")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Summary",
            "Keywords",
            "Analysis",
            "Quiz",
            "Statistics"
        ]
    )

    with tab1:

        st.header("Paper Summary")

        st.write(summary)

    with tab2:

        st.header("Keywords")

        st.write(keywords)

        fig = keyword_chart(keywords)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab3:

        st.header("Research Objective")

        st.info(objective)

        st.header("Limitations")

        if limitations:

            for item in limitations:
                st.write("•", item)

        else:
            st.write("No limitations detected.")

    with tab4:

        st.header("Generated Quiz")

        for i, question in enumerate(quiz, 1):

            st.write(
                f"Q{i}: {question}"
            )

    with tab5:

        st.header("Paper Statistics")

        st.metric(
            "Words",
            stats["Words"]
        )

        st.metric(
            "Characters",
            stats["Characters"]
        )

        st.metric(
            "Sentences",
            stats["Sentences"]
        )