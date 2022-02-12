from fastapi import FastAPI
import spacy

app = FastAPI()

nlp = spacy.load("en_core_web_sm")

@app.get("/{textInit}")
async def analyzeText(textInit):
    doc = nlp(textInit)

    analyzedText = ''

    for ent in doc.ents:
        analyzedText += ent.text + '->' + ent.label_ + ', '

    return analyzedText[0:-2]
