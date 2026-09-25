import json

from .attraction import Attraction
from .user import User


attraction_file = "data/attractions.json"
users_file = "data/users.json"


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

    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
