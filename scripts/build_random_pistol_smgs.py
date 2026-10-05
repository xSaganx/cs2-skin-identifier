#!/usr/bin/env python3
"""Build a CS2 skin database with real skin names for pistols and SMGs."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "skins.json"

REAL_SKINS = [
    {"weapon": "Glock-18", "name": "Dragon Tattoo", "rarity": "Mil-Spec"},
    {"weapon": "Glock-18", "name": "Wasteland Rebel", "rarity": "Mil-Spec"},
    {"weapon": "Glock-18", "name": "Graven", "rarity": "Restricted"},
    {"weapon": "Glock-18", "name": "Bullet Queen", "rarity": "Mil-Spec"},
    {"weapon": "Glock-18", "name": "Nightmare", "rarity": "Restricted"},
    {"weapon": "Glock-18", "name": "Ironwork", "rarity": "Mil-Spec"},
    {"weapon": "P2000", "name": "Amber Fade", "rarity": "Restricted"},
    {"weapon": "P2000", "name": "Corticera", "rarity": "Mil-Spec"},
    {"weapon": "P2000", "name": "Red Fragcam", "rarity": "Mil-Spec"},
    {"weapon": "P2000", "name": "Ocean Foam", "rarity": "Restricted"},
    {"weapon": "USP-S", "name": "Caiman", "rarity": "Restricted"},
    {"weapon": "USP-S", "name": "Cyrex", "rarity": "Classified"},
    {"weapon": "USP-S", "name": "Blood Tiger", "rarity": "Mil-Spec"},
    {"weapon": "USP-S", "name": "Printstream", "rarity": "Restricted"},
    {"weapon": "USP-S", "name": "Road Rash", "rarity": "Mil-Spec"},
    {"weapon": "P250", "name": "Undertow", "rarity": "Mil-Spec"},
    {"weapon": "P250", "name": "Asiimov", "rarity": "Classified"},
    {"weapon": "P250", "name": "Whiteout", "rarity": "Restricted"},
    {"weapon": "P250", "name": "Supernova", "rarity": "Mil-Spec"},
    {"weapon": "P250", "name": "Franklin", "rarity": "Restricted"},
    {"weapon": "Desert Eagle", "name": "Sunset Storm", "rarity": "Restricted"},
    {"weapon": "Desert Eagle", "name": "Nored", "rarity": "Mil-Spec"},
    {"weapon": "Desert Eagle", "name": "Midnight Storm", "rarity": "Mil-Spec"},
    {"weapon": "Desert Eagle", "name": "Code Red", "rarity": "Restricted"},
    {"weapon": "Five-SeveN", "name": "Fairytale", "rarity": "Restricted"},
    {"weapon": "Five-SeveN", "name": "Monkey Business", "rarity": "Mil-Spec"},
    {"weapon": "Five-SeveN", "name": "Kami", "rarity": "Mil-Spec"},
    {"weapon": "Five-SeveN", "name": "Triumvirate", "rarity": "Restricted"},
    {"weapon": "Tec-9", "name": "Titanium Burst", "rarity": "Restricted"},
    {"weapon": "Tec-9", "name": "Re-Entry", "rarity": "Mil-Spec"},
    {"weapon": "Tec-9", "name": "Bamboozle", "rarity": "Restricted"},
    {"weapon": "MP5-SD", "name": "Condition Zero", "rarity": "Restricted"},
    {"weapon": "MP5-SD", "name": "Liquidation", "rarity": "Mil-Spec"},
    {"weapon": "MP5-SD", "name": "Acid Wash", "rarity": "Mil-Spec"},
    {"weapon": "MP7", "name": "Nemesis", "rarity": "Restricted"},
    {"weapon": "MP7", "name": "Bloodstream", "rarity": "Restricted"},
    {"weapon": "MP7", "name": "Aftermarket", "rarity": "Mil-Spec"},
    {"weapon": "MP9", "name": "Starlight Protector", "rarity": "Restricted"},
    {"weapon": "MP9", "name": "Hot Rod", "rarity": "Restricted"},
    {"weapon": "MP9", "name": "Airlock", "rarity": "Mil-Spec"},
    {"weapon": "UMP-45", "name": "Primal Saber", "rarity": "Restricted"},
    {"weapon": "UMP-45", "name": "Blaze", "rarity": "Restricted"},
    {"weapon": "UMP-45", "name": "Momentum", "rarity": "Mil-Spec"},
    {"weapon": "MAC-10", "name": "Neon Rider", "rarity": "Restricted"},
    {"weapon": "MAC-10", "name": "Disco Tech", "rarity": "Restricted"},
    {"weapon": "MAC-10", "name": "Heat", "rarity": "Mil-Spec"},
    {"weapon": "PP-Bizon", "name": "Fuel Rod", "rarity": "Mil-Spec"},
    {"weapon": "PP-Bizon", "name": "Photic Zone", "rarity": "Mil-Spec"},
    {"weapon": "PP-Bizon", "name": "Antique", "rarity": "Mil-Spec"},
    {"weapon": "P90", "name": "Asiimov", "rarity": "Classified"},
    {"weapon": "P90", "name": "Shapewood", "rarity": "Restricted"},
    {"weapon": "P90", "name": "Emerald Dragon", "rarity": "Mil-Spec"},
]


def build_signature(weapon: str, skin_name: str) -> list:
    combined = f"{weapon}_{skin_name}".encode()
    sig = []
    for byte in combined[:32]:
        sig.append(byte % 256)
    while len(sig) < 32:
        sig.append(0)
    return sig[:32]


def build_database():
    skins = []
    for skin_data in REAL_SKINS:
        skin = {
            "name": f"{skin_data['weapon']} | {skin_data['name']}",
            "weapon": skin_data["weapon"],
            "skin_name": skin_data["name"],
            "rarity": skin_data["rarity"],
            "signature": build_signature(skin_data["weapon"], skin_data["name"]),
        }
        skins.append(skin)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps({"skins": skins}, indent=2), encoding="utf-8")
    print(f"Built {len(skins)} real CS2 pistol/SMG skins.")
    print(f"Saved to {DATA_FILE}")


if __name__ == "__main__":
    build_database()
