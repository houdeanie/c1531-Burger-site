# initlialise system and enter menu items
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
from src.menu_creator import *

def bootstrap_system():
    system = GourmetBurgerSystem(create_menu())
    return system

def bootstrap_order():
    new_order = Order()
    return new_order