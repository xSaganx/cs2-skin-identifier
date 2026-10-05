from __future__ import annotations

import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_FILE = DATA_DIR / "skins.json"


def build_template_dataset():
    dataset = {
        "skins": [
            {
                "name": "AK-47 | Neon Rider",
                "weapon": "AK-47",
                "signature": [98, 124, 149, 167, 175, 47, 86, 96, 122, 88, 72, 52, 69, 89, 126, 73, 121, 154, 132, 197, 203, 79, 97, 111, 42, 57, 65, 91, 56, 77, 88, 101],
                "palette": ["#5a6f8c", "#93a4b4", "#d9a764", "#2b3d52"],
                "texture": "bright",
            }
        ]
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(dataset, indent=2), encoding="utf-8")
    print(f"Dataset written to: {DATA_FILE}")


if __name__ == "__main__":
    build_template_dataset()
