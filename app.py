
### 🧩 app.py
```python
from fastapi import FastAPI, Form
import openai, os

app = FastAPI(title="LLM Contract Summarizer")

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/summarize")
def summarize_contract(text: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Summarize contracts in structured format."},
            {"role": "user", "content": text}
        ]
    )
    return {"summary": response.choices[0].message["content"]}
  
