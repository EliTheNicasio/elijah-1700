from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/{remText}")
async def readText(remText):
    return {"message": "Look: " + remText}
