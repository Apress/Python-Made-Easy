class Gear:
    def get_number_of_gears(self):
        print(f"Has 12 gears")

class Mountainbike():
    def __init__(self, gear):
        self.gear = gear

    def get_number_of_gears(self):
        self.gear.get_number_of_gears()

class Roadbike():
    def get_number_of_gears(self):
        print(f"Has 2 times 11 gears")
        
my_mountainbike = Mountainbike(Gear())
my_mountainbike.get_number_of_gears() # Has 12 gears
my_roadbike = Roadbike()
my_roadbike.get_number_of_gears() # Has 2 times 11 gears