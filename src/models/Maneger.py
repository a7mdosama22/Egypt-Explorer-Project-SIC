import json
from attraction import Attraction

attraction_file = 'data\\attractions.json'

def load_attractions():
    with open(attraction_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    return [Attraction.from_dict(item) for item in raw_data]


def save_attractions(attractions):
    data = [a.to_dict() for a in attractions]
    with open(attraction_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)