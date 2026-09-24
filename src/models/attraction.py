"""
Attraction model.
Shared by everyone — read this file first.
"""


class Attraction:
    def __init__(self, id, name, governorate, ticket_price,
                 rating, estimated_visit_time, category):
        self.id = id
        self.name = name
        self.governorate = governorate
        self.ticket_price = ticket_price
        self.rating = rating
        self.estimated_visit_time = estimated_visit_time
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "governorate": self.governorate,
            "ticket_price": self.ticket_price,
            "rating": self.rating,
            "estimated_visit_time": self.estimated_visit_time,
            "category": self.category,
        }

    @staticmethod
    def from_dict(data):
        return Attraction(
            id=data.get("id"),
            name=data.get("name"),
            governorate=data.get("governorate"),
            ticket_price=data.get("ticket_price"),
            rating=data.get("rating"),
            estimated_visit_time=data.get("estimated_visit_time"),
            category=data.get("category"),
        )

    def __str__(self):
        return (f"{self.name} - {self.ticket_price} EGP - "
                f"⭐{self.rating} ({self.governorate})")

    def full_details(self):
        return (
            f"Name: {self.name}\n"
            f"Governorate: {self.governorate}\n"
            f"Ticket Price: {self.ticket_price} EGP\n"
            f"Rating: {self.rating}\n"
            f"Estimated Visit Time: {self.estimated_visit_time}\n"
            f"Category: {self.category}"
        )
