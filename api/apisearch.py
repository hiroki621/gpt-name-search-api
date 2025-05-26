from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

dict_path = os.path.join(os.path.dirname(__file__), '..', 'horse_name_dictionary.json')
with open(dict_path, encoding="utf-8") as f:
    DICTIONARY = json.load(f)

@app.get("/api/search")
def search_dictionary(theme: str = Query(...), limit: int = 5):
    results = []
    for entry in DICTIONARY:
        if theme in entry["romaji"] or theme in entry["kana"]:
            results.append(entry)
        if len(results) >= limit:
            break
    return JSONResponse(content=results)
