from src.menu import *

def create_menu():
	menu = Menu() 
		
	#add mains to menu
	menu.add_main("custom burger", 0, 500, "main", {}) 
	menu.add_main("base burger", 7, 500, "main", {"sesame bun": 2, "beef patty": 1, "tomato": 1, "lettuce": 1, "swiss cheese": 1, "ians special sauce": 1}) 
	menu.add_main("custom wrap", 0, 1000, "main", {}) 
	menu.add_main("base wrap", 6, 1000, "main", {"white wrap": 1, "veg filling": 1, "tomato": 1, "lettuce": 1, "swiss cheese": 1, "ians special sauce": 1}) 

	#add ingredients to menu		
	menu.add_menu_item("sesame bun", 1, 1000, "ingredient", "burger", "bun")
	menu.add_menu_item("muffin bun", 1.50, 1000, "ingredient", "burger", "bun") 
	menu.add_menu_item("beef patty", 1.5, 1000, "ingredient", "burger", "patty")
	menu.add_menu_item("veg patty", 1, 1000, "ingredient", "burger", "patty") 
	menu.add_menu_item("white wrap", 1.00, 1000, "ingredient", "wrap", "wrap") 
	menu.add_menu_item("wholemeal wrap", 1.00, 1000, "ingredient", "wrap", "wrap") 
	menu.add_menu_item("tuna filling", 1.5, 1000, "ingredient", "wrap", "filling") 
	menu.add_menu_item("veg filling", 1.5, 1000, "ingredient", "wrap", "filling") 
	menu.add_menu_item("tomato", 0.5, 1000, "ingredient", "burger, wrap", "vegetable") 
	menu.add_menu_item("lettuce", 0.5, 1000, "ingredient", "burger, wrap", "vegetable")
	menu.add_menu_item("swiss cheese", 0.5, 1000, "ingredient", "burger, wrap", "cheese") 
	menu.add_menu_item("cheddar cheese", 0.5, 1000, "ingredient", "burger, wrap", "cheese") 
	menu.add_menu_item("tomato sauce", 0.5, 1000, "ingredient", "burger, wrap", "sauce")
	menu.add_menu_item("ians special sauce", 2, 1000, "ingredient", "burger, wrap", "sauce") 

	#add sides
	menu.add_base_item("nuggets", 0, 1000, "side", ["small nuggets", "medium nuggets", "large nuggets"])
	menu.add_measured_item("small nuggets", 3.0, -1, "side", 3, "nuggets") 
	menu.add_measured_item("medium nuggets", 5.0, -1, "side", 6, "nuggets")
	menu.add_measured_item("large nuggets", 7.0, -1, "side", 10, "nuggets") 
	menu.set_quantity("nuggets")
	menu.add_base_item("fries", 0, 6000, "side", ["small fries", "medium fries", "large fries"])
	menu.add_measured_item("small fries", 2.5, -1, "side", 75, "fries")
	menu.add_measured_item("medium fries", 3.5, -1, "side", 150, "fries")
	menu.add_measured_item("large fries", 4.5, -1, "side", 250, "fries")
	menu.set_quantity("fries")
	
	#add drinks 
	menu.add_menu_item("water", 3.0, 1000, "drink", None, None)
	menu.add_base_item("orange juice", 0, 10000, "drink", ["small orange juice", "medium orange juice",  "large orange juice"])
	menu.add_measured_item("small orange juice", 2.5, -1, "drink", 250, "orange juice") 
	menu.add_measured_item("medium orange juice", 3.5,  -1, "drink", 450, "orange juice")
	menu.add_measured_item("large orange juice", 4.5, -1, "drink", 650, "orange juice")
	menu.set_quantity("orange juice")

	#add sundaes
	menu.add_base_item("sundae", 0, 10000, "dessert", ["small chocolate sundae", "medium chocolate sundae", "large chocolate sundae", "small strawberry sundae", "medium strawberry sundae", "large strawberry sundae"])
	menu.add_measured_item("small chocolate sundae", 3.5, -1, "dessert", 250, "sundae") 
	menu.add_measured_item("medium chocolate sundae", 4.5, -1, "dessert", 450, "sundae") 
	menu.add_measured_item("large chocolate sundae", 5.5, -1, "dessert", 650, "sundae") 	
	menu.add_measured_item("small strawberry sundae", 3.5, -1, "dessert", 250, "sundae") 	
	menu.add_measured_item("medium strawberry sundae", 4.5, -1, "dessert", 450, "sundae")
	menu.add_measured_item("large strawberry sundae", 5.5, -1, "dessert", 650, "sundae") 	
	menu.set_quantity("sundae")
									
	return menu