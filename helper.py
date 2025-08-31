from transformers import pipeline
from datasets import Dataset
import fitz  
import os

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        text = ""
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def chunk_text(text,max_words=400):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i:i+max_words]))
    return chunks

def summarize_batch(batch):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summaries = summarizer(batch["text"], 
                           max_length=30, 
                           min_length=10, 
                           do_sample=False)
    return {"summary": [s["summary_text"] for s in summaries]}

def tokenize(example):
            return {"length": len(example["text"])}
        