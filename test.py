# test.py for testing things
from src.menu import *
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
from src.menu_creator import *
from src.item import *


# testing creating a simple order of a burger
system = GourmetBurgerSystem(create_menu())
print(system.display_inventory)
ingredients = system.display_inventory.get_measured_item('side')

ingredient = system.display_item('lettuce')

print(ingredients)
print(len(ingredients))
print(ingredient)



