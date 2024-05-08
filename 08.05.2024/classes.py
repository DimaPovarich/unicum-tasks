class Car:
    def __init__(self, model, make, engine_volume, color):
        self.model = model
        self.make = make
        self.engine_volume = engine_volume
        self.color = color

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def __eq__(self, other):
        return self.model == other.model and self.make == other.make and self.engine_volume == other.engine_volume and self.color == other.color

    def __lt__(self, other):
        return self.engine_volume < other.engine_volume

    def __gt__(self, other):
        return self.engine_volume > other.engine_volume
car1 = Car("Mersedes", 2002, 312, "White")
car2 = Car("BMW", 2010, 348, "Black")

print(car1 == car2)
print(car1 < car2)
