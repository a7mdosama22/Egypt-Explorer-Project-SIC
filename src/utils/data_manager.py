"""
Generic JSON load/save helpers.
Owner: Member 1 (Auth) — shared by everyone.
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")
ATTRACTIONS_FILE = os.path.join(DATA_DIR, "attractions.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")


def load_json(filepath):
    """Load a JSON file and return its content (list or dict)."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath, data):
    """Save data (list or dict) to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_attractions():
    from src.models.attraction import Attraction
    raw = load_json(ATTRACTIONS_FILE)
    return [Attraction.from_dict(item) for item in raw]


def save_attractions(attractions):
    save_json(ATTRACTIONS_FILE, [a.to_dict() for a in attractions])


def load_users():
    from src.models.user import User
    raw = load_json(USERS_FILE)
    return [User.from_dict(item) for item in raw]


def save_users(users):
    save_json(USERS_FILE, [u.to_dict() for u in users])
