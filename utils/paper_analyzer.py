import re


def extract_objective(text):

    patterns = [
        "this study",
        "this paper",
        "our objective",
        "aim of this study",
        "research aims"
    ]

    sentences = text.split(".")

    for sentence in sentences:

        lower = sentence.lower()

        if any(pattern in lower for pattern in patterns):
            return sentence.strip()

    return "Objective not automatically detected."


def extract_limitations(text):

    limitations = []

    sentences = text.split(".")

    keywords = [
        "limitation",
        "limited",
        "small dataset",
        "future work"
    ]

    for sentence in sentences:

        lower = sentence.lower()

        if any(keyword in lower for keyword in keywords):
            limitations.append(sentence.strip())

    return limitations[:10]


def paper_statistics(text):

    words = len(text.split())

    chars = len(text)

    sentences = len(re.split(r'[.!?]', text))

    return {
        "Words": words,
        "Characters": chars,
        "Sentences": sentences
    }