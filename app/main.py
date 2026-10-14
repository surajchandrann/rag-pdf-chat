from fastapi import FastAPI
app= FastAPI(title="PDF CHAT")

@app.get("/health")
def health():
    return {"status":"ok"}
