class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

bus = Bus(seating_capacity=50)
print(f"Total fare for the bus: {bus.calculate_fare()}")
