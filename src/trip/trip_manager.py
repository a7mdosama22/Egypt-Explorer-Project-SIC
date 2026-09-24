"""
My Trip management + Final Trip Summary calculation.
Owner: Member 3

IMPORTANT: the final cost must NOT be hard-coded — it must be recomputed
from whatever is currently in the trip, using a non-iterative approach
(e.g. sum() with a generator/map instead of a manual for-loop with +=).
"""

# Flat transportation-cost lookup table by governorate.
# TODO: tune these numbers / agree on them as a team.
TRANSPORT_COST_BY_GOVERNORATE = {
    "Cairo": 50,
    "Giza": 60,
    "Alexandria": 150,
    "Luxor": 300,
    "Aswan": 350,
    "South Sinai": 400,
    "Matrouh": 350,
    "New Valley": 380,
    "Fayoum": 120,
}
DEFAULT_TRANSPORT_COST = 200


class TripManager:
    def __init__(self):
        self.selected_attractions = []  # list[Attraction]

    def add_to_trip(self, attraction):
        if attraction not in self.selected_attractions:
            self.selected_attractions.append(attraction)

    def remove_from_trip(self, attraction):
        if attraction in self.selected_attractions:
            self.selected_attractions.remove(attraction)

    def view_trip(self):
        return self.selected_attractions

    def calculate_attractions_cost(self):
        """Non-iterative sum of ticket prices."""
        return sum(a.ticket_price for a in self.selected_attractions)

    def calculate_transportation_cost(self):
        """
        Non-iterative: sum a per-attraction transport cost, looked up
        by governorate, deduplicated by governorate so the user isn't
        charged multiple times for attractions in the same governorate.
        """
        governorates = {a.governorate for a in self.selected_attractions}
        return sum(
            TRANSPORT_COST_BY_GOVERNORATE.get(g, DEFAULT_TRANSPORT_COST)
            for g in governorates
        )

    def get_final_summary(self):
        attractions_cost = self.calculate_attractions_cost()
        transportation_cost = self.calculate_transportation_cost()
        return {
            "attractions": self.selected_attractions,
            "attractions_cost": attractions_cost,
            "transportation_cost": transportation_cost,
            "total_cost": attractions_cost + transportation_cost,
        }
