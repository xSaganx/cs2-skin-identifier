#!/usr/bin/env python3
"""Build a focused CS2 skin dataset for pistols and SMGs only."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "skins.json"

WEAPON_LIST = [
    "Glock-18", "P2000", "USP-S", "P250", "Desert Eagle", "Tec-9", "Five-SeveN",
    "MP5-SD", "MP7", "MP9", "UMP-45", "MAC-10", "PP-Bizon", "P90"
]

RANDOM_SKINS = [
    "Ashen Echo", "Dust Fade", "Vein Drift", "Graphite Pulse", "Sable Alloy", "Molten Current",
    "Rift Burn", "Cold Signal", "Beryl Mist", "Night Circuit", "Chrome Echo", "Signal Bloom",
    "Rust Grain", "Frost Arc", "Steel Thread", "Amber Signal", "Cinder Trace", "Blue Ember",
    "Slate Mirage", "Circuit Ash", "Quiet Surge", "Glass Echo", "Dust Circuit", "Signal Vein",
    "Red Noise", "Night Thread", "Grain Pulse", "Coarse Shadow", "Monsoon Core", "Firn Drift",
    "Urban Haze", "Signal Mist", "Carbon Bloom", "Copper Dusk", "Dust Echo", "Hollow Steel",
    "Patina Shift", "Mist Arc", "Broken Circuit", "Cinder Omen", "Ash Trail", "Metal Vein",
    "Ghost Harbor", "Blue Static", "Iron Silence", "Ferro Shade", "Dark Valve", "Cold Echo",
    "Apex Rust", "Shiver Coil", "Copper Noise", "Smoke Thread", "Noir Circuit", "Steel Pulse",
    "Dust Reactor", "Gravel Bloom", "Midnight Thread", "Signal Drift", "Ashen Wire", "Rust Circuit",
    "Night Polarity", "Frost Signal", "Obsidian Thread", "Cinder Bloom", "Steel Mist", "Haze Circuit",
    "Ferro Current", "Dust Prism", "Velvet Static", "Rusted Vein", "Cold Drift", "Low Signal"
]

PALETTES = [
    ["#4d4d4d", "#7f7f7f", "#d9d9d9", "#1a1a1a"],
    ["#0d3b66", "#1f78b4", "#bde0fe", "#0c0c0c"],
    ["#4d2c18", "#b5651d", "#f4d35e", "#222222"],
    ["#3a3a3a", "#8fbc8f", "#d1f2a5", "#000000"],
    ["#5e2a2a", "#b22222", "#ff6b6b", "#1b1b1b"],
    ["#2b2d42", "#8d99ae", "#edf2f4", "#111111"],
    ["#7b2cbf", "#c77dff", "#f1c0e8", "#181818"],
    ["#006466", "#5bc0be", "#d8f3dc", "#111827"],
    ["#7f5539", "#d4a373", "#f6e7d8", "#231815"],
    ["#2f3e46", "#cad2c5", "#84a98c", "#111111"],
    ["#1f2937", "#3b82f6", "#93c5fd", "#020617"],
    ["#3c096c", "#9d4edd", "#f3e8ff", "#0f0f0f"],
    ["#a4161a", "#ef233c", "#ffb3c1", "#111111"],
    ["#7f8c8d", "#dfe6e9", "#b2bec3", "#2d3436"],
    ["#3d405b", "#81b29a", "#f2cc8f", "#0f172a"],
    ["#14213d", "#fca311", "#e5e5e5", "#000000"],
    ["#2b2d42", "#ffb703", "#f5f3f4", "#111111"],
    ["#1f1f1f", "#f0f0f0", "#7f7f7f", "#0a0a0a"],
    ["#1d3557", "#457b9d", "#a8dadc", "#031926"],
    ["#264653", "#2a9d8f", "#e9c46a", "#111111"]
]

TEXTURES = [
    "matte", "grit", "metal", "dust", "polished", "granular", "weathered",
    "muted", "rough", "grained", "dark", "industrial", "simple", "glossy"
]


def build_signature(palette):
    colors = []
    for hex_color in palette:
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        colors.append((r, g, b))

    avg = tuple(sum(c[i] for c in colors) // len(colors) for i in range(3))
    sig = []
    for c in colors:
        sig.extend(c)
    sig.extend(avg)
    sig.extend([
        abs(colors[0][0] - avg[0]),
        abs(colors[0][1] - avg[1]),
        abs(colors[0][2] - avg[2]),
        sum(avg) // 3,
        (avg[0] + avg[1]) // 2,
        (avg[1] + avg[2]) // 2,
        (avg[0] + avg[2]) // 2,
        max(avg),
        min(avg),
        abs(max(avg) - min(avg)),
        255 - avg[0],
        255 - avg[1],
        255 - avg[2],
    ])
    return sig[:32]


def build_database():
    skins = []
    for weapon_index, weapon in enumerate(WEAPON_LIST):
        for skin_index in range(18):
            name = RANDOM_SKINS[(weapon_index * 18 + skin_index) % len(RANDOM_SKINS)]
            palette = PALETTES[(weapon_index + skin_index) % len(PALETTES)]
            skin = {
                "name": f"{weapon} | {name}",
                "weapon": weapon,
                "palette": palette,
                "texture": TEXTURES[(weapon_index + skin_index) % len(TEXTURES)],
                "signature": build_signature(palette),
            }
            skins.append(skin)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps({"skins": skins}, indent=2), encoding="utf-8")
    print(f"Built {len(skins)} pistol/SMG skin entries.")
    print(f"Saved to {DATA_FILE}")


if __name__ == "__main__":
    build_database()
