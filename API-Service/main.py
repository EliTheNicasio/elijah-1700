from fastapi import FastAPI

app = FastAPI()

@app.get("/{textInit}")
async def analyzeText(textInit):
    return {"message": "MF_" + textInit}
