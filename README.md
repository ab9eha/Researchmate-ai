 # ResearchMate AI 📚

An AI-powered research assistant that helps students and researchers analyze academic papers through automatic summarization, keyword extraction, objective detection, limitation analysis, quiz generation, and interactive visualizations.

## 🚀 Features

* 📄 Upload research papers in PDF format
* 📝 Automatic paper summarization
* 🔑 Keyword extraction and analysis
* 🎯 Research objective detection
* ⚠️ Limitation identification
* ❓ Quiz generation for study and revision
* 📊 Interactive keyword visualizations
* 📈 Research paper statistics dashboard
* 🌐 Streamlit-based user interface

## 🛠️ Technology Stack

* Python
* Streamlit
* PyMuPDF
* Sumy
* NLTK
* Scikit-Learn
* Pandas
* Plotly
* NumPy
* TextStat

## 📂 Project Structure

```text
researchmate-ai
│
├── app.py
├── requirements.txt
├── README.md
├── nltk_setup.py
│
├── data
│   └── .gitkeep
│
├── utils
│   ├── pdf_processor.py
│   ├── summarizer.py
│   ├── keyword_extractor.py
│   ├── quiz_generator.py
│   ├── paper_analyzer.py
│   └── visualization.py
│
└── assets
    └── .gitkeep
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/researchmate-ai.git
cd researchmate-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download required NLTK resources:

```bash
python nltk_setup.py
```

Run the application:

```bash
python -m streamlit run app.py
```

## 🎓 Use Cases

* Research paper analysis
* Literature review support
* Academic study assistance
* Research topic exploration
* Student learning and revision
* Knowledge extraction from scholarly articles

## 📊 Workflow

```text
PDF Upload
    ↓
Text Extraction
    ↓
Summarization
    ↓
Keyword Analysis
    ↓
Objective & Limitation Detection
    ↓
Quiz Generation
    ↓
Visualization Dashboard
```

## 🔮 Future Enhancements

* Multi-paper comparison
* Citation extraction
* Research trend analysis
* AI-powered question answering
* Export reports to PDF
* Research recommendation engine

## 👨‍💻 Author

Developed as an AI and NLP portfolio project demonstrating research analysis, natural language processing, and data visualization techniques.

## 📜 License

This project is intended for educational and portfolio purposes.
