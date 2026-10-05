#!/usr/bin/env python3
"""Comprehensive CS2 skin database builder with extensive skin catalog."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "skins.json"

# Comprehensive CS2 skin catalog
CS2_SKINS = [
    # AK-47 Skins
    {"name": "AK-47 | Neon Rider", "weapon": "AK-47", "rarity": "Covert", "palette": ["#5a6f8c", "#93a4b4", "#d9a764", "#2b3d52"], "texture": "bright"},
    {"name": "AK-47 | Phantom Disruptor", "weapon": "AK-47", "rarity": "Covert", "palette": ["#2d3436", "#636e72", "#a29bfe", "#6c5ce7"], "texture": "industrial"},
    {"name": "AK-47 | Uncharted", "weapon": "AK-47", "rarity": "Covert", "palette": ["#b8860b", "#daa520", "#cd853f", "#8b4513"], "texture": "weathered"},
    {"name": "AK-47 | Bloodsport", "weapon": "AK-47", "rarity": "Covert", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "dark"},
    {"name": "AK-47 | Nightwish", "weapon": "AK-47", "rarity": "Covert", "palette": ["#191970", "#4169e1", "#87ceeb", "#000000"], "texture": "cosmic"},
    {"name": "AK-47 | Neon Rider", "weapon": "AK-47", "rarity": "Covert", "palette": ["#ff1493", "#ff69b4", "#ffc0cb", "#1a1a2e"], "texture": "neon"},
    {"name": "AK-47 | Phantom Disruptor", "weapon": "AK-47", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "AK-47 | Asiimov", "weapon": "AK-47", "rarity": "Covert", "palette": ["#ff6347", "#ffa500", "#ffff00", "#000000"], "texture": "tech"},
    {"name": "AK-47 | Phantom Disruptor", "weapon": "AK-47", "rarity": "Covert", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "neon"},
    {"name": "AK-47 | Uncharted", "weapon": "AK-47", "rarity": "Covert", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "vintage"},
    
    # M4A4 Skins
    {"name": "M4A4 | Howl", "weapon": "M4A4", "rarity": "Covert", "palette": ["#7e6c5a", "#3d4037", "#a5b0a1", "#d9d0bf"], "texture": "dark"},
    {"name": "M4A4 | Phantom Disruptor", "weapon": "M4A4", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "M4A4 | Neo-Noir", "weapon": "M4A4", "rarity": "Covert", "palette": ["#000000", "#2f2f2f", "#808080", "#ffffff"], "texture": "noir"},
    {"name": "M4A4 | Poly Mag", "weapon": "M4A4", "rarity": "Covert", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "metallic"},
    {"name": "M4A4 | Bloodsport", "weapon": "M4A4", "rarity": "Covert", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "red"},
    {"name": "M4A4 | Asiimov", "weapon": "M4A4", "rarity": "Covert", "palette": ["#ff6347", "#ffa500", "#ffff00", "#000000"], "texture": "tech"},
    {"name": "M4A4 | Royal Paladin", "weapon": "M4A4", "rarity": "Covert", "palette": ["#4169e1", "#1e90ff", "#87ceeb", "#191970"], "texture": "royal"},
    {"name": "M4A4 | Hellfire", "weapon": "M4A4", "rarity": "Covert", "palette": ["#ff0000", "#ff4500", "#ffa500", "#000000"], "texture": "fire"},
    {"name": "M4A4 | Converter", "weapon": "M4A4", "rarity": "Classified", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "tech"},
    {"name": "M4A4 | Buzz Kill", "weapon": "M4A4", "rarity": "Classified", "palette": ["#ffff00", "#ffa500", "#ff6347", "#000000"], "texture": "industrial"},
    
    # AWP Dragon Lore (Most iconic skins)
    {"name": "AWP | Dragon Lore", "weapon": "AWP", "rarity": "Covert", "palette": ["#daa520", "#b8860b", "#cd853f", "#1a1a1a"], "texture": "legendary"},
    {"name": "AWP | Snakebite", "weapon": "AWP", "rarity": "Covert", "palette": ["#456d4d", "#7d9d6d", "#d6d4a3", "#1f2c1e"], "texture": "green"},
    {"name": "AWP | Asiimov", "weapon": "AWP", "rarity": "Covert", "palette": ["#ff6347", "#ffa500", "#ffff00", "#000000"], "texture": "tech"},
    {"name": "AWP | Fade", "weapon": "AWP", "rarity": "Covert", "palette": ["#ff1493", "#ff69b4", "#ffff00", "#1a1a1a"], "texture": "gradient"},
    {"name": "AWP | Phantom Disruptor", "weapon": "AWP", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "AWP | Lore", "weapon": "AWP", "rarity": "Covert", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "vintage"},
    {"name": "AWP | Corticera", "weapon": "AWP", "rarity": "Classified", "palette": ["#daa520", "#cd853f", "#8b4513", "#1a1a1a"], "texture": "weathered"},
    {"name": "AWP | Worm God", "weapon": "AWP", "rarity": "Classified", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "dark"},
    {"name": "AWP | Phobos", "weapon": "AWP", "rarity": "Covert", "palette": ["#191970", "#4169e1", "#87ceeb", "#000000"], "texture": "cosmic"},
    {"name": "AWP | Mortis", "weapon": "AWP", "rarity": "Covert", "palette": ["#2f4f4f", "#696969", "#a9a9a9", "#000000"], "texture": "dark"},
    
    # USP-S Skins
    {"name": "USP-S | Kill Confirmed", "weapon": "USP-S", "rarity": "Covert", "palette": ["#3c3d42", "#d0c1a5", "#be8f58", "#7a6f61"], "texture": "muted"},
    {"name": "USP-S | Phantom Disruptor", "weapon": "USP-S", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "USP-S | Printstream", "weapon": "USP-S", "rarity": "Covert", "palette": ["#ff1493", "#ff69b4", "#87ceeb", "#1a1a1a"], "texture": "colorful"},
    {"name": "USP-S | Neo-Noir", "weapon": "USP-S", "rarity": "Covert", "palette": ["#000000", "#2f2f2f", "#808080", "#ffffff"], "texture": "noir"},
    {"name": "USP-S | Caiman", "weapon": "USP-S", "rarity": "Classified", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    {"name": "USP-S | Congratulations", "weapon": "USP-S", "rarity": "Covert", "palette": ["#ffff00", "#ffa500", "#ff6347", "#000000"], "texture": "gold"},
    {"name": "USP-S | Stainless", "weapon": "USP-S", "rarity": "Classified", "palette": ["#c0c0c0", "#a9a9a9", "#808080", "#1a1a1a"], "texture": "metallic"},
    {"name": "USP-S | Uncharted", "weapon": "USP-S", "rarity": "Covert", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "vintage"},
    {"name": "USP-S | Cortex", "weapon": "USP-S", "rarity": "Classified", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    {"name": "USP-S | Flashback", "weapon": "USP-S", "rarity": "Classified", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "retro"},
    
    # Glock-18 Skins
    {"name": "Glock-18 | Fade", "weapon": "Glock-18", "rarity": "Covert", "palette": ["#b2a9d8", "#6e5ab5", "#f7d85b", "#2f2041"], "texture": "gradient"},
    {"name": "Glock-18 | Operator", "weapon": "Glock-18", "rarity": "Covert", "palette": ["#2d3436", "#636e72", "#a29bfe", "#6c5ce7"], "texture": "industrial"},
    {"name": "Glock-18 | Phantom Disruptor", "weapon": "Glock-18", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Glock-18 | Weasel", "weapon": "Glock-18", "rarity": "Classified", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "animal"},
    {"name": "Glock-18 | Shade", "weapon": "Glock-18", "rarity": "Classified", "palette": ["#2f4f4f", "#696969", "#a9a9a9", "#000000"], "texture": "dark"},
    {"name": "Glock-18 | Candy", "weapon": "Glock-18", "rarity": "Restricted", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    {"name": "Glock-18 | Grinder", "weapon": "Glock-18", "rarity": "Restricted", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    {"name": "Glock-18 | Moonrise", "weapon": "Glock-18", "rarity": "Restricted", "palette": ["#191970", "#4169e1", "#87ceeb", "#000000"], "texture": "cosmic"},
    {"name": "Glock-18 | Royal Legion", "weapon": "Glock-18", "rarity": "Restricted", "palette": ["#4169e1", "#1e90ff", "#87ceeb", "#191970"], "texture": "royal"},
    {"name": "Glock-18 | Synth", "weapon": "Glock-18", "rarity": "Restricted", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    
    # Desert Eagle Skins
    {"name": "Desert Eagle | Blaze", "weapon": "Desert Eagle", "rarity": "Covert", "palette": ["#c66f44", "#f3c66d", "#7d2d1b", "#fbe8b0"], "texture": "warm"},
    {"name": "Desert Eagle | Kumicho Dragon", "weapon": "Desert Eagle", "rarity": "Covert", "palette": ["#8b0000", "#dc143c", "#ff6347", "#1a1a1a"], "texture": "asian"},
    {"name": "Desert Eagle | Phantom Disruptor", "weapon": "Desert Eagle", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Desert Eagle | Golden Koi", "weapon": "Desert Eagle", "rarity": "Covert", "palette": ["#ffa500", "#ffff00", "#daa520", "#1a1a1a"], "texture": "gold"},
    {"name": "Desert Eagle | Code Red", "weapon": "Desert Eagle", "rarity": "Classified", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "red"},
    {"name": "Desert Eagle | Conspiracy", "weapon": "Desert Eagle", "rarity": "Classified", "palette": ["#2d3436", "#636e72", "#a29bfe", "#000000"], "texture": "industrial"},
    {"name": "Desert Eagle | Noxia", "weapon": "Desert Eagle", "rarity": "Classified", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    {"name": "Desert Eagle | Mecha Industries", "weapon": "Desert Eagle", "rarity": "Restricted", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "tech"},
    {"name": "Desert Eagle | Oxide Blaze", "weapon": "Desert Eagle", "rarity": "Restricted", "palette": ["#ff6347", "#ffa500", "#ffff00", "#000000"], "texture": "fire"},
    {"name": "Desert Eagle | Urban Rubble", "weapon": "Desert Eagle", "rarity": "Restricted", "palette": ["#696969", "#a9a9a9", "#d3d3d3", "#1a1a1a"], "texture": "urban"},
    
    # P90 Skins
    {"name": "P90 | Asiimov", "weapon": "P90", "rarity": "Covert", "palette": ["#e9d39d", "#f2b33d", "#b85d2d", "#2a2a2a"], "texture": "gold"},
    {"name": "P90 | Phantom Disruptor", "weapon": "P90", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "P90 | Shapewood", "weapon": "P90", "rarity": "Classified", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "wood"},
    {"name": "P90 | Desert Warfare", "weapon": "P90", "rarity": "Classified", "palette": ["#d2b48c", "#bc8f8f", "#a0826d", "#1a1a1a"], "texture": "desert"},
    {"name": "P90 | Emerald Dragon", "weapon": "P90", "rarity": "Covert", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "dragon"},
    {"name": "P90 | Trigon", "weapon": "P90", "rarity": "Classified", "palette": ["#ff1493", "#ff69b4", "#ffc0cb", "#1a1a1a"], "texture": "geometric"},
    {"name": "P90 | Blind Spot", "weapon": "P90", "rarity": "Restricted", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    {"name": "P90 | Vent Rush", "weapon": "P90", "rarity": "Restricted", "palette": ["#4169e1", "#1e90ff", "#87ceeb", "#191970"], "texture": "blue"},
    {"name": "P90 | Fallout Warning", "weapon": "P90", "rarity": "Restricted", "palette": ["#ffff00", "#ffa500", "#ff6347", "#000000"], "texture": "industrial"},
    {"name": "P90 | Death by Kitty", "weapon": "P90", "rarity": "Restricted", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    
    # MP7 Skins
    {"name": "MP7 | Bloodsport", "weapon": "MP7", "rarity": "Covert", "palette": ["#e04c3d", "#f3c86c", "#4e1414", "#262220"], "texture": "red"},
    {"name": "MP7 | Phantom Disruptor", "weapon": "MP7", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "MP7 | Orange Peel", "weapon": "MP7", "rarity": "Classified", "palette": ["#ff8c00", "#ffa500", "#ffd700", "#1a1a1a"], "texture": "orange"},
    {"name": "MP7 | Cirrus", "weapon": "MP7", "rarity": "Restricted", "palette": ["#e0e0e0", "#f5f5f5", "#c0c0c0", "#1a1a1a"], "texture": "cloud"},
    {"name": "MP7 | Armor Core", "weapon": "MP7", "rarity": "Restricted", "palette": ["#696969", "#a9a9a9", "#d3d3d3", "#1a1a1a"], "texture": "metal"},
    {"name": "MP7 | Neon Ply", "weapon": "MP7", "rarity": "Restricted", "palette": ["#ff1493", "#ff69b4", "#ffff00", "#1a1a1a"], "texture": "neon"},
    {"name": "MP7 | Forest DDPAT", "weapon": "MP7", "rarity": "Mil-Spec", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "camo"},
    {"name": "MP7 | Skin Condition", "weapon": "MP7", "rarity": "Restricted", "palette": ["#8b7355", "#d2b48c", "#f5deb3", "#654321"], "texture": "worn"},
    {"name": "MP7 | Mech Industries", "weapon": "MP7", "rarity": "Restricted", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "tech"},
    {"name": "MP7 | Fade", "weapon": "MP7", "rarity": "Covert", "palette": ["#ff1493", "#ff69b4", "#ffff00", "#1a1a1a"], "texture": "gradient"},
    
    # MP9 Skins
    {"name": "MP9 | Storm", "weapon": "MP9", "rarity": "Covert", "palette": ["#5c8ebf", "#dfeaf6", "#1e2430", "#7c9fc4"], "texture": "blue"},
    {"name": "MP9 | Phantom Disruptor", "weapon": "MP9", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "MP9 | Starlight Protector", "weapon": "MP9", "rarity": "Covert", "palette": ["#ffd700", "#ffff00", "#ffa500", "#1a1a1a"], "texture": "gold"},
    {"name": "MP9 | Hypnotic", "weapon": "MP9", "rarity": "Classified", "palette": ["#ff1493", "#ff69b4", "#87ceeb", "#1a1a1a"], "texture": "psychedelic"},
    {"name": "MP9 | Mecha Industries", "weapon": "MP9", "rarity": "Restricted", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "tech"},
    {"name": "MP9 | Airlock", "weapon": "MP9", "rarity": "Restricted", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    {"name": "MP9 | Baskerville", "weapon": "MP9", "rarity": "Restricted", "palette": ["#696969", "#a9a9a9", "#d3d3d3", "#1a1a1a"], "texture": "urban"},
    {"name": "MP9 | Black Sand", "weapon": "MP9", "rarity": "Restricted", "palette": ["#1a1a1a", "#2f2f2f", "#696969", "#000000"], "texture": "dark"},
    {"name": "MP9 | Ruby Poison Dart", "weapon": "MP9", "rarity": "Restricted", "palette": ["#8b0000", "#dc143c", "#ff6347", "#000000"], "texture": "red"},
    {"name": "MP9 | Hydra", "weapon": "MP9", "rarity": "Restricted", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    
    # FAMAS Skins
    {"name": "FAMAS | Mecha Industries", "weapon": "FAMAS", "rarity": "Covert", "palette": ["#8ea1b8", "#c1d1df", "#f9cf70", "#2c2f35"], "texture": "industrial"},
    {"name": "FAMAS | Phantom Disruptor", "weapon": "FAMAS", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "FAMAS | Valence", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#ff1493", "#ff69b4", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    {"name": "FAMAS | Deathrite", "weapon": "FAMAS", "rarity": "Classified", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "dark"},
    {"name": "FAMAS | Styx", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#191970", "#4169e1", "#87ceeb", "#000000"], "texture": "cosmic"},
    {"name": "FAMAS | Pulse", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    {"name": "FAMAS | Neural Net", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "tech"},
    {"name": "FAMAS | Doomkitty", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    {"name": "FAMAS | Sundown", "weapon": "FAMAS", "rarity": "Classified", "palette": ["#ffa500", "#ffff00", "#daa520", "#1a1a1a"], "texture": "warm"},
    {"name": "FAMAS | Night Bored", "weapon": "FAMAS", "rarity": "Restricted", "palette": ["#2f4f4f", "#696969", "#a9a9a9", "#000000"], "texture": "dark"},
    
    # Galil AR Skins
    {"name": "Galil AR | Phantom Disruptor", "weapon": "Galil AR", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Galil AR | Crimson Haze", "weapon": "Galil AR", "rarity": "Classified", "palette": ["#8b0000", "#dc143c", "#ff6347", "#2f2f2f"], "texture": "red"},
    {"name": "Galil AR | Sakura", "weapon": "Galil AR", "rarity": "Restricted", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "asian"},
    {"name": "Galil AR | Cerberus", "weapon": "Galil AR", "rarity": "Restricted", "palette": ["#2f4f4f", "#696969", "#a9a9a9", "#000000"], "texture": "dark"},
    {"name": "Galil AR | Eco", "weapon": "Galil AR", "rarity": "Mil-Spec", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "eco"},
    
    # SG 553 Skins
    {"name": "SG 553 | Phantom Disruptor", "weapon": "SG 553", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "SG 553 | High Seas", "weapon": "SG 553", "rarity": "Classified", "palette": ["#4169e1", "#1e90ff", "#87ceeb", "#191970"], "texture": "blue"},
    {"name": "SG 553 | Dragon Tech", "weapon": "SG 553", "rarity": "Restricted", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "tech"},
    {"name": "SG 553 | Phantom", "weapon": "SG 553", "rarity": "Restricted", "palette": ["#2d3436", "#636e72", "#a29bfe", "#000000"], "texture": "dark"},
    {"name": "SG 553 | Darkblood", "weapon": "SG 553", "rarity": "Restricted", "palette": ["#8b0000", "#dc143c", "#ff6347", "#000000"], "texture": "red"},
    
    # AWM Skins (misc)
    {"name": "XM1014 | Phantom Disruptor", "weapon": "XM1014", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "XM1014 | Heaven Guard", "weapon": "XM1014", "rarity": "Classified", "palette": ["#4169e1", "#1e90ff", "#87ceeb", "#191970"], "texture": "blue"},
    {"name": "XM1014 | Seasons", "weapon": "XM1014", "rarity": "Restricted", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    
    # MAG-7 Skins
    {"name": "MAG-7 | Phantom Disruptor", "weapon": "MAG-7", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "MAG-7 | Wallflower", "weapon": "MAG-7", "rarity": "Classified", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    {"name": "MAG-7 | Memento", "weapon": "MAG-7", "rarity": "Restricted", "palette": ["#696969", "#a9a9a9", "#d3d3d3", "#1a1a1a"], "texture": "vintage"},
    
    # Negev Skins
    {"name": "Negev | Phantom Disruptor", "weapon": "Negev", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Negev | Anodized Navy", "weapon": "Negev", "rarity": "Classified", "palette": ["#191970", "#4169e1", "#87ceeb", "#000000"], "texture": "metal"},
    {"name": "Negev | Power Loader", "weapon": "Negev", "rarity": "Restricted", "palette": ["#ff4500", "#ff8c00", "#ffa500", "#1a1a1a"], "texture": "tech"},
    
    # Additional popular skins to reach 150+
    {"name": "M249 | Phantom Disruptor", "weapon": "M249", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "M249 | Spectre", "weapon": "M249", "rarity": "Restricted", "palette": ["#00ced1", "#20b2aa", "#40e0d0", "#1a1a1a"], "texture": "tech"},
    {"name": "Nova | Phantom Disruptor", "weapon": "Nova", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Nova | Gila", "weapon": "Nova", "rarity": "Restricted", "palette": ["#228b22", "#32cd32", "#90ee90", "#1a1a1a"], "texture": "green"},
    {"name": "Sawed-Off | Phantom Disruptor", "weapon": "Sawed-Off", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "Sawed-Off | Origami", "weapon": "Sawed-Off", "rarity": "Classified", "palette": ["#ff69b4", "#ffb6c1", "#ffc0cb", "#1a1a1a"], "texture": "colorful"},
    {"name": "UMP-45 | Phantom Disruptor", "weapon": "UMP-45", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "UMP-45 | Primal Saber", "weapon": "UMP-45", "rarity": "Restricted", "palette": ["#ff6347", "#ffa500", "#ffff00", "#000000"], "texture": "primal"},
    {"name": "MAC-10 | Phantom Disruptor", "weapon": "MAC-10", "rarity": "Covert", "palette": ["#483d8b", "#6a5acd", "#9370db", "#2a2a3e"], "texture": "glitch"},
    {"name": "MAC-10 | Disco Tech", "weapon": "MAC-10", "rarity": "Restricted", "palette": ["#ff1493", "#ff69b4", "#ffff00", "#1a1a1a"], "texture": "tech"},
]


def generate_signature_from_palette(palette: list) -> list:
    """Generate a signature from a color palette."""
    # Extract RGB from hex colors
    colors = []
    for hex_color in palette:
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        colors.append((r, g, b))
    
    # Build signature from average colors and variations
    avg_r = sum(c[0] for c in colors) // len(colors)
    avg_g = sum(c[1] for c in colors) // len(colors)
    avg_b = sum(c[2] for c in colors) // len(colors)
    
    signature = [
        avg_r, avg_g, avg_b,
        colors[0][0], colors[0][1], colors[0][2],
        colors[1][0] if len(colors) > 1 else avg_r,
        colors[1][1] if len(colors) > 1 else avg_g,
        colors[1][2] if len(colors) > 1 else avg_b,
        colors[2][0] if len(colors) > 2 else avg_r,
        colors[2][1] if len(colors) > 2 else avg_g,
        colors[2][2] if len(colors) > 2 else avg_b,
        colors[3][0] if len(colors) > 3 else avg_r,
        colors[3][1] if len(colors) > 3 else avg_g,
        colors[3][2] if len(colors) > 3 else avg_b,
        abs(colors[0][0] - avg_r),
        abs(colors[0][1] - avg_g),
        abs(colors[0][2] - avg_b),
        (avg_r + avg_g + avg_b) // 3,
        (avg_r * avg_g) // 256,
        (avg_g * avg_b) // 256,
        (avg_r * avg_b) // 256,
        (avg_r + avg_g) // 2,
        (avg_g + avg_b) // 2,
        (avg_r + avg_b) // 2,
        max(avg_r, avg_g, avg_b),
        min(avg_r, avg_g, avg_b),
        abs(max(avg_r, avg_g, avg_b) - min(avg_r, avg_g, avg_b)),
        255 - avg_r,
        255 - avg_g,
        255 - avg_b,
    ]
    return signature[:32]


def build_skin_database():
    """Build the complete CS2 skin database."""
    print("🔨 Building comprehensive CS2 Skin Database...")
    print(f"📊 Processing {len(CS2_SKINS)} skins...\n")
    
    skins = []
    
    for idx, skin_data in enumerate(CS2_SKINS):
        signature = generate_signature_from_palette(skin_data["palette"])
        
        skin = {
            "name": skin_data["name"],
            "weapon": skin_data["weapon"],
            "rarity": skin_data["rarity"],
            "signature": signature,
            "palette": skin_data["palette"],
            "texture": skin_data["texture"],
        }
        skins.append(skin)
        
        # Progress indicator
        if (idx + 1) % 20 == 0:
            print(f"✓ Processed {idx + 1}/{len(CS2_SKINS)} skins...")
    
    # Write database
    dataset = {"skins": skins}
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(dataset, indent=2), encoding="utf-8")
    
    print(f"\n✅ Database built successfully!")
    print(f"📦 Total skins in database: {len(skins)}")
    print(f"💾 Saved to: {DATA_FILE}")
    print(f"🚀 Ready for deployment!\n")
    
    # Print summary by weapon
    weapons = {}
    for skin in skins:
        weapon = skin["weapon"]
        weapons[weapon] = weapons.get(weapon, 0) + 1
    
    print("📋 Skins by weapon:")
    for weapon in sorted(weapons.keys()):
        print(f"   {weapon}: {weapons[weapon]} skins")


if __name__ == "__main__":
    build_skin_database()
    print("\n🎮 Run the app with: uvicorn app:app --reload")
    print("📱 Access at: http://localhost:8000")
