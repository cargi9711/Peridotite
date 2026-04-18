class Peridotite:
    def __init__(self, name, composition, density):
        self.name = name
        self.composition = composition
        self.density = density

    def describe(self):
        return f"{self.name} is composed of {self.composition} with density {self.density} g/cm³."

    def __str__(self):
        return f"{self.name} | Composition: {self.composition} | Density: {self.density}"
