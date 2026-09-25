import json
import os

from .attraction import Attraction
from .user import User


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(CURRENT_DIR)
BASE_DIR = os.path.dirname(SRC_DIR)

attraction_file = os.path.join(BASE_DIR, "data", "attractions.json")
users_file = os.path.join(BASE_DIR, "data", "users.json")


def load_attractions():
    try:
        with open(attraction_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not raw_data:
        return []

    return [Attraction.from_dict(item) for item in raw_data]


def save_attractions(attractions):
    data = [a.to_dict() for a in attractions]

    os.makedirs(os.path.dirname(attraction_file), exist_ok=True)

    with open(attraction_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_users():
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not raw_data:
        return []

    return [User.from_dict(item) for item in raw_data]


def save_users(users):
    data = [user.to_dict() for user in users]

    os.makedirs(os.path.dirname(users_file), exist_ok=True)

    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)