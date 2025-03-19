class Passenger:
    passenger_names = []
    total_weight = 46

#initialize Passenger attributes
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def weight_count(self):
        if self.weight > Passenger.total_weight:
            print(f"{self.name}: Too much weight")
        else:
            print(f"{self.name} carrying  {self.weight} kg")

arnold = Passenger("arnold", 32)
bruno = Passenger("bruno", 120)

arnold.weight_count()
bruno.weight_count()