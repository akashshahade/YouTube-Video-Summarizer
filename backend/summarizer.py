import requests
import os
from dotenv import load_dotenv

# Load API key from .env file (if exists)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

def summarize_text(text):
    """
    Summarizes the input text using Groq's LLaMA3-8B model.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"  # ✅ Corrected URL
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama3-8b-8192",  # ✅ Correct Groq model name
        "messages": [
            {"role": "system", "content": "Summarize the following text in bullet points."},
            {"role": "user", "content": text},
        ],
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.json()}"
