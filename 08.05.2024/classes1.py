class DistanceConverter:
    def __init__(self, kilometers):
        self.kilometers = kilometers

    def to_meters(self):
        return self.kilometers * 1000

    def to_yards(self):
        return self.kilometers * 1093.61

    def to_miles(self):
        return self.kilometers * 0.621371

    def to_centimeters(self):
        return self.kilometers * 100000

    def to_inches(self):
        return self.kilometers * 39370.1

    def to_feet(self):
        return self.kilometers * 3280.84

    def to_nautical_miles(self):
        return self.kilometers * 0.539957

    def __str__(self):
        return (f"{self.kilometers} kilometers\n" 
               f"{self.to_meters()} meters\n" 
               f"{self.to_yards()} yards\n" 
               f"{self.to_miles()} miles\n" 
               f"{self.to_centimeters()} centimeters\n" 
               f"{self.to_inches()} inches\n" 
               f"{self.to_feet()} feet\n" 
               f"{self.to_nautical_miles()} nautical miles")
converter = DistanceConverter(int(input("Enter any distance in kilometers: ")))
print(converter)
