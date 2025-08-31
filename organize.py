
import os
import shutil
from dotenv import load_dotenv
from groq import Groq
import glob
from helper import *
from categorize import categorize



load_dotenv()
client = Groq(
    api_key=os.environ.get("KEY"),
)
def organize(path,categories=None):
    files = glob.glob(path+"/**/*.pdf", recursive=True) + glob.glob(path+"/**/*.txt", recursive=True)

    if categories is not None:
        categories = [c.strip() for c in str(categories).split(",")]
        categories.append("Other")
    else:
        cat_text = categorize(path)
        categories = [c.strip() for c in cat_text.split(",")]
        categories.append("Other")
    results = []
    for f in files:
        text = extract_text(f)
        if not text.strip():
            continue

        chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert that classifies research papers."},
                {"role": "user", "content": f"""
    Paper: {text[:2000]}

    Task: Assign this paper to ONE of the following categories:
    {', '.join(categories)}

    Answer with exactly one category name.
                """}
            ]
        )

        label = chat_completion.choices[0].message.content.strip()
        if label not in categories:
            label = "Other"

        results.append((f, label))

        target_dir = os.path.join(path, label)
        file_name = os.path.basename(f)
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(f, os.path.join(target_dir, file_name))
        
    print("Classification Results:")
    for r in results:
        print(os.path.basename(r[0]) + ": " + r[1])