# initlialise system and enter menu items
from src.gourmetBurgerSystem import *


def bootstrap_system():

    system = GourmetBurgerSystem()
    return system
'''
    rego = 0
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore", "Buggy"]:
            system.add_car(SmallCar(name, model, str(rego)))
            rego += 1
            system.add_car(MediumCar(name, model, str(rego)))
            rego += 1
            system.add_car(LargeCar(name, model, str(rego)))
            rego += 1

    for name in ["Tesla", "Audi", "Mercedes"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, str(rego)))
            rego += 1 
'''