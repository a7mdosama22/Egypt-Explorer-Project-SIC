"""
Admin Panel: add / update / delete attractions.
Owner: Member 4
"""

from src.models.attraction import Attraction
from src.utils.data_manager import load_attractions, save_attractions


def add_attraction(name, governorate, ticket_price, rating,
                    estimated_visit_time, category):
    attractions = load_attractions()
    new_id = max((a.id for a in attractions), default=0) + 1
    new_attraction = Attraction(
        id=new_id, name=name, governorate=governorate,
        ticket_price=ticket_price, rating=rating,
        estimated_visit_time=estimated_visit_time, category=category,
    )
    attractions.append(new_attraction)
    save_attractions(attractions)
    return new_attraction


def update_attraction(attraction_id, **fields):
    """
    fields: any of name, governorate, ticket_price, rating,
            estimated_visit_time, category
    """
    attractions = load_attractions()
    for a in attractions:
        if a.id == attraction_id:
            for key, value in fields.items():
                if hasattr(a, key):
                    setattr(a, key, value)
            save_attractions(attractions)
            return a
    return None  # not found


def delete_attraction(attraction_id):
    attractions = load_attractions()
    remaining = [a for a in attractions if a.id != attraction_id]
    if len(remaining) == len(attractions):
        return False  # nothing was removed
    save_attractions(remaining)
    return True
