class Mineral:
    def __init__(self, name, hardness):
        self.name = name
        self.hardness = hardness

    def info(self):
        return f"{self.name} has a hardness of {self.hardness} on the Mohs scale."
