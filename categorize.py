import os
from dotenv import load_dotenv
from groq import Groq
import glob
from helper import *
from datasets.utils.logging import disable_progress_bar
disable_progress_bar()
from tqdm import tqdm
load_dotenv()
client = Groq(
    api_key=os.environ.get("KEY"),
)
def categorize(path):
   
    files = glob.glob(path+"**/*.pdf", recursive=True) + glob.glob(path+"**/*.txt", recursive=True)
    summaries = []
    print("Summarizing Files")
    for f in tqdm(files):
        text = extract_text(f)
        chunks = chunk_text(text)
        dataset = Dataset.from_dict({"text": chunks})
        new_dataset = dataset.map(summarize_batch, batched=True, batch_size=8)
        file_summary = []
        for item in new_dataset:
            file_summary.append(item["summary"])
        file_summary = [s for sublist in file_summary for s in sublist]
        summaries.append((f," ".join(file_summary)))
        
    summary_text = "\n".join([f"{f_name}: {s}" for f_name, s in summaries])
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Here are summaries of papers:\n{summary_text}\n\nSuggest useful ways to categorize them into groups, write useful ways separated by '\n' and categories separated by comma. if exist consider research area, document title, purpose of file. Answer with exactly one series of categories."}
        ],
    model="llama-3.3-70b-versatile",
    )
    response = chat_completion.choices[0].message.content
    return response