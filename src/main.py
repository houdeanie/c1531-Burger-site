from gourmetBurgerSystem import GourmetBurgerSystem
from menu_creator import *
system = GourmetBurgerSystem(create_menu())

items = system.get_menu_items()
for each in sorted(items.keys()):
	menu_item = items[each]
	print("name: {0}, quantity: {1}, price: ${2}".format(menu_item._name, menu_item._stock_quantity, menu_item._price))

