from gourmetBurgerSystem import GourmetBurgerSystem

system = GourmetBurgerSystem()

items = system.get_menu_items()
for each in sorted(items.keys()):
	menu_item = items[each]
    print("name:",menu_item._name)
    print("quantity:",menu_item._quantity)
    print("price:",menu_item._price)	
