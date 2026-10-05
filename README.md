# CS2 Skin Identifier

AI-powered MVP for identifying CS2 skins from uploaded images or fragments.

## What it does
- accepts an uploaded image of a CS2 skin or a close crop/fragment
- compares it against a locally prepared skin database
- returns the most likely match immediately
- works fast because it does not search the internet live

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open: http://localhost:8000/

## Deploy to Railway

1. Create a new Railway project
2. Connect this repository
3. Use the default Python service
4. Railway will run:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

## Important note
This is a fast MVP based on a precomputed skin signature database. It is optimized for speed and local matching, which is the right architecture for a production skin recognizer.

To scale to thousands of skins, expand `data/skins.json` with more entries and tune the signature logic.
