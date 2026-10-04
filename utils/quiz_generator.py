import re


def generate_quiz(text):

    sentences = re.split(r'[.!?]', text)

    quiz_questions = []

    for sentence in sentences[:20]:

        words = sentence.split()

        if len(words) > 8:

            question = (
                f"What is discussed in the following statement?\n\n"
                f"{sentence.strip()}?"
            )

            quiz_questions.append(question)

    return quiz_questions[:10]