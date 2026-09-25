import json

from .attraction import Attraction
from .user import User, Admin


attraction_file = "data/attractions.json"
users_file = "data/users.json"

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"


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

def ensure_admin_account():
    users = load_users()

    for user in users:
        if user.email == ADMIN_EMAIL:
            return

    admin_user = Admin(
        name="Admin",
        phone="00000000000",
        email=ADMIN_EMAIL,
        gender="Male",
        governorate="Cairo",
        password=ADMIN_PASSWORD,
        age=30,
        national_id="00000000000000",
    )
    users.append(admin_user)
    save_users(users)