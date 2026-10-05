# CS2 Skin Identifier

A production-ready web app scaffold for identifying CS2 skins from uploaded images or crop fragments.

## What this project is
This repository contains:
- a FastAPI backend for image upload and prediction
- a browser UI for uploading skin images
- a local skin database with vector-like color signatures
- a dataset build script for adding more skins later
- a Railway deployment configuration

## Important note
This project is built as a real recognition system with a scalable database pipeline. It does not magically contain every CS2 skin without a dataset source. To support the full CS2 skin catalog, you provide or import the skin image dataset and run the data builder script.

The project is structured so that expanding to all skins is straightforward and fast.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open:
- http://localhost:8000/

## Railway deployment
Use the included `railway.json` and deploy the repo as a Python service.

Recommended command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

## Dataset preparation
Run the dataset builder when you add more skin data:

```bash
python scripts/build_skin_dataset.py
```

This script prepares the data used by the matcher.

## Production idea
For a full-scale version with all CS2 skins, use a real skin image corpus and generate signatures for each skin image. Then the app simply compares a user-provided crop against the precomputed database and returns the most likely match in milliseconds.
