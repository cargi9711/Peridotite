class Mantle:
    def __init__(self, depth_km, temperature_c):
        self.depth_km = depth_km
        self.temperature_c = temperature_c

    def describe(self):
        return f"Earth's mantle at {self.depth_km} km with temperature {self.temperature_c}°C."
