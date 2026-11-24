from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from app import extract, llm, storage

app = FastAPI(title="BriefAI")

@app.get("/", response_class=HTMLResponse)
def index():
    with open("app/templates/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/api/summarize")
async def summarize_file(file: UploadFile = File(...)):
    data = await file.read()
    text = extract.extract_text(file.filename, data)
    summary = llm.make_summary(text)
    return storage.save(file.filename, summary)

@app.get("/api/model-check")
def model_check():
    answer = llm.ask_model("Ответь одним словом: ты работаешь?")
    return {"model_answer": answer}
