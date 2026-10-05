from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DATA_FILE = BASE_DIR / "data" / "skins.json"

app = FastAPI(title="CS2 Skin Identifier")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

with DATA_FILE.open("r", encoding="utf-8") as f:
    SKINS = json.load(f)["skins"]


def normalize_image(image: Image.Image) -> np.ndarray:
    resized = ImageOps.fit(image.convert("RGB"), (128, 128), method=Image.Resampling.LANCZOS)
    return np.asarray(resized, dtype=np.float32)


def image_signature(image: Image.Image) -> np.ndarray:
    arr = normalize_image(image)
    avg = arr.mean(axis=(0, 1))
    hist_r = np.histogram(arr[:, :, 0], bins=8, range=(0, 256))[0] / 1000
    hist_g = np.histogram(arr[:, :, 1], bins=8, range=(0, 256))[0] / 1000
    hist_b = np.histogram(arr[:, :, 2], bins=8, range=(0, 256))[0] / 1000
    brightness = arr.mean(axis=2)
    variance = np.var(brightness)

    signature = np.concatenate([
        avg,
        hist_r,
        hist_g,
        hist_b,
        np.array([variance], dtype=np.float32),
    ]).astype(np.float32)
    return signature


def match_skin(uploaded_signature: np.ndarray):
    candidates = []
    for skin in SKINS:
        skin_signature = np.asarray(skin["signature"], dtype=np.float32)
        distance = float(np.linalg.norm(uploaded_signature[:32] - skin_signature[:32]))
        candidates.append({\n            "name": skin["name"],
            "weapon": skin["weapon"],
            "texture": skin["texture"],
            "palette": skin.get("palette", []),
            "distance": distance,
        })

    sorted_candidates = sorted(candidates, key=lambda item: item["distance"])
    return sorted_candidates[:5], sorted_candidates[0]


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/skins")
def list_skins():
    return {"skins": [{"name": skin["name"], "weapon": skin["weapon"]} for skin in SKINS]}


@app.post("/api/identify")
async def identify_skin(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    try:
        image = Image.open(file.file)
        signature = image_signature(image)
        matches, best = match_skin(signature)
        return {
            "best_match": {
                "name": best["name"],
                "weapon": best["weapon"],
                "texture": best["texture"],
                "confidence": round(max(0.0, 100.0 - (best["distance"] / 10.0)), 2),
                "palette": best["palette"],
            },
            "matches": matches,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Could not read image: {str(exc)}") from exc
