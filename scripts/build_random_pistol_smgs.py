# CS2 Skin Identifier

A lightweight CS2 skin recognizer focused on pistols and SMGs.

## Scope
This version intentionally focuses on:
- pistols
- SMGs
- no stickers
- no cases
- no knife-heavy metadata
- random skin names and palette-based signatures

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_random_pistol_smgs.py
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Then open:
- http://localhost:8000/

## Railway
Use the included `railway.json` to deploy this app.
