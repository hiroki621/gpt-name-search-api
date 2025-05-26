from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# ファイル読み込み（辞書のロード）
dict_path = os.path.join(os.path.dirname(__file__), '..', 'horse_name_dictionary.json')
with open(dict_path, encoding="utf-8") as f:
    DICTIONARY = json.load(f)

@app.get("/api/search")
def search_dictionary(
    themes: list[str] = Query(..., description="検索テーマのリスト（複数指定可）"),
    limit: int = 5
):
    results = []
    used_ids = set()

    for theme in themes:
        for entry in DICTIONARY:
            if theme in entry["romaji"] or theme in entry["kana"]:
                if entry["id"] not in used_ids:
                    results.append(entry)
                    used_ids.add(entry["id"])
                if len(results) >= limit:
                    return JSONResponse(content=results)

    return JSONResponse(content=results)
