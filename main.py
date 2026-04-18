from peridotite import Peridotite
from mantle import Mantle

rock = Peridotite("Lherzolite", "Olivine + Pyroxene", 3.3)
mantle = Mantle(100, 1300)

print(rock)
print(rock.describe())
print(mantle.describe())
