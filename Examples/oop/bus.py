from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__()
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus()
bus1.add_warning('Test')
bus1.add_group(['Susanne', 'Felix', 'Luis'])
print(bus1.passengers)
print(bus1.get_warnings())

