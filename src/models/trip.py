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

class Trip:
    def __init__(self):
        self.selected_attractions = []   

    def add_attraction(self, attraction):
        if attraction not in self.selected_attractions:
            self.selected_attractions.append(attraction)
            return True
        return False   

    def remove_attraction(self, attraction):
        if attraction in self.selected_attractions:
            self.selected_attractions.remove(attraction)
            return True
        return False   

    def view_trip(self):
        return self.selected_attractions

    def is_empty(self):
        return len(self.selected_attractions) == 0

    def calculate_attractions_cost(self):
        return sum(a.ticket_price for a in self.selected_attractions)

    def calculate_transportation_cost(self):
        governorates = {a.governorate for a in self.selected_attractions}
        return sum(
            TRANSPORT_COST_BY_GOVERNORATE.get(g, DEFAULT_TRANSPORT_COST)
            for g in governorates)

    def get_summary(self):
        attractions_cost = self.calculate_attractions_cost()
        transportation_cost = self.calculate_transportation_cost()
        return {
            "attractions": self.selected_attractions,
            "attractions_cost": attractions_cost,
            "transportation_cost": transportation_cost,
            "total_cost": attractions_cost + transportation_cost,
        }

    def clear(self):
        self.selected_attractions = []