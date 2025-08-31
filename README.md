# 📂 Sortify — AI-Powered File Organizer

**Sortify** is an AI-powered tool that helps you **summarize, categorize, and organize your PDF and text files** into folders using **LLMs**.

## </> Demo
```
# Unorganized files
~/sortify/files$ ls
Alice_in_Wonderland.pdf  Attention_Is_All_You_Need.pdf  Intro_To_RL.pdf  Segment_Anything.pdf

# Organizing files
~/sortify$ python main.py -cmd organize -dir ./files/ -cat "NLP, Computer_Vision, Reinforcement_Learning, Other"
Classification Results:
Segment_Anything.pdf: Computer_Vision
Intro_To_RL.pdf: Reinforcement_Learning
Attention_Is_All_You_Need.pdf: NLP
Alice_in_Wonderland.pdf: Other

# Organized directories
~/sortify/files$ ls
Computer_Vision  NLP  Other  Reinforcement_Learning

# Directory structure
~/sortify/files$ tree .
.
├── Computer_Vision
│   └── Segment_Anything.pdf
├── NLP
│   └── Attention_Is_All_You_Need.pdf
├── Other
│   └── Alice_in_Wonderland.pdf
└── Reinforcement_Learning
    └── Intro_To_RL.pdf

5 directories, 4 files
```

---

## ✨ Features

* 📄 **Supports PDFs & TXT files** — automatic text extraction
* ✂️ **Chunking** — splits large documents for efficient processing
* 📝 **Summarization** — uses Hugging Face's summarization pipeline with `facebook/bart-large-cnn` to generate concise summaries for category generation.
* 🧠 **LLM-assisted categorization** — leverages summaries + **Groq’s LLaMA models** to:

  * Suggest useful categories for your collection
  * Classify each document into the best matching category
* 📂 **Smart file organization** — moves files into category-based folders automatically


---

## 🔍 How It Works

1. Extracts text from `.pdf` and `.txt` files
2. Splits content into manageable chunks
3. Generates summaries with Hugging Face’s **BART** model
4. Uses summaries + **Groq LLaMA** for categorization
5. Moves files into their assigned category folders

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/sajjadim/sortify.git
   cd sortify
   ```

2. Create a virtual environment & install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux  
   venv\Scripts\activate      # Windows  

   pip install -r requirements.txt
   ```

3. Add your **Groq API key** to a `.env` file:

   ```
   KEY=your_groq_api_key_here
   ```

---

## ▶️ Usage

### 1. Generate Suggested Categories

```bash
python main.py --command categories --directory ./papers/
```

### 2. Organize Papers Automatically

```bash
python main.py --command organize --directory ./papers/
```

### 3. Use Custom Categories

```bash
python main.py --command organize --directory ./papers/ --categories "AI, Healthcare, Finance"
```



## 📦 Requirements

* Python 3.9+
* [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`)
* [transformers](https://huggingface.co/transformers/)
* [datasets](https://huggingface.co/docs/datasets/)
* [groq](https://groq.com/) SDK
* `python-dotenv`

---

## ⚠️ Limitations

* Summaries may miss nuances for very long documents
* Categorization depends on summary quality & LLaMA responses
* Requires **Groq API access**

Perfect 🙌 those are great roadmap items. Adding a **“Future Work”** section in your README not only shows vision but also attracts contributors. Here’s how you can extend your README 👇

---

## 🚀 Future Work

* 🎥 **Multimedia support**

  * Extract and analyze content from images, audio, and video files (e.g., OCR for images, speech-to-text for audio/video).

* 🔎 **Global semantic search**

  * Build an embedding-based index across all files for powerful semantic search, making it easy to find concepts instead of just keywords.

* ❓ **Question Answering (QA) over documents**

  * Ask natural language questions about your collection and receive grounded answers, powered by retrieval + LLMs.

