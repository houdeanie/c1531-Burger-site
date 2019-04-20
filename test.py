# test.py for testing things
from src.menu import *
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
from src.menu_creator import *
from src.item import *
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order

'''
	menu.add_menu_item("sesame bun", 1, 1000, "ingredient", "burger")
	menu.add_menu_item("muffin bun", 1.50, 1000, "ingredient", "burger") 
	menu.add_menu_item("beef patty", 1.5, 1000, "ingredient", "burger")
	menu.add_menu_item("veg patty", 1, 1000, "ingredient", "burger") 
	menu.add_menu_item("white wrap", 1.00, 1000, "ingredient", "wrap") 
	menu.add_menu_item("wholemeal wrap", 1.00, 1000, "ingredient", "wrap") 
	menu.add_menu_item("tuna filling", 1.5, 1000, "ingredient", "wrap") 
	menu.add_menu_item("veg filling", 1.5, 1000, "ingredient", "wrap") 
	menu.add_menu_item("tomato", 0.5, 1000, "ingredient", "burger, wrap") 
	menu.add_menu_item("lettuce", 0.5, 1000, "ingredient", "burger, wrap")
	menu.add_menu_item("swiss cheese", 0.5, 1000, "ingredient", "burger, wrap") 
	menu.add_menu_item("cheddar cheese", 0.5, 1000, "ingredient", "burger, wrap") 
	menu.add_menu_item("tomato sauce", 0.5, 1000, "ingredient", "burger, wrap")
	menu.add_menu_item("ians pecial sauce", 2, 1000, "ingredient", "burger, wrap") 
'''
# testing creating a simple order of a burger
system = GourmetBurgerSystem(create_menu())
print(system.display_inventory)

order = system.new_order()


burger = system.new_main_order_item("Burger")
burger.add_ingredient("sesame bun", system.display_inventory.get_price("sesame bun"))

order.add_item(burger, system.display_inventory.get_price("sesame bun"))

order.add_item
print(order)


