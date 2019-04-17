from menu import *

def create_menu():
	menu = Menu() 
	#add mains to menu
	menu.add_main("custom burger", 0, 500, "main", []) 
	menu.add_main("base burger", 7, 500, "main", ["sesame bun", "sesame bun", "beef patty", "tomato", "lettuce", "swiss cheese", "ians special sauce"]) 
	menu.add_main("custom wrap", 0, 1000, "main", []) 
	menu.add_main("base wrap", 6, 1000, "main", ["white wrap", "veg filling", "tomato", "lettuce", "swiss cheese", "ians special sauce"]) 
		
	#add ingredients to menu		
	menu.add_menu_item("sesame bun", 1, 1000, "ingredient")
	menu.add_menu_item("muffin bun", 1.50, 1000, "ingredient") 
	menu.add_menu_item("beef patty", 1.5, 1000, "ingredient") 
	menu.add_menu_item("veg patty", 1, 1000, "ingredient") 
	menu.add_menu_item("white wrap", 1.00, 1000, "ingredient") 
	menu.add_menu_item("wholemeal wrap", 1.00, 1000, "ingredient") 
	menu.add_menu_item("tuna filling", 1.5, 1000, "ingredient") 
	menu.add_menu_item("veg filling", 1.5, 1000, "ingredient") 
	menu.add_menu_item("tomato", 0.5, 1000, "ingredient") 
	menu.add_menu_item("lettuce", 0.5, 1000, "ingredient")
	menu.add_menu_item("swiss cheese", 0.5, 1000, "ingredient") 
	menu.add_menu_item("cheddar cheese", 0.5, 1000, "ingredient") 
	menu.add_menu_item("tomato sauce", 0.5, 1000, "ingredient")
	menu.add_menu_item("ians pecial sauce", 2, 1000, "ingredient") 
	
	#add sides
	menu.add_base_item("nugget", 0, 1000, "side", ["small nuggets", "medium nuggets", "large nuggets"])
	set_quantity("nugget")
	menu.add_measured_item("small nuggets", 3.0, -1, "side", 3, "nuggets") 
	menu.add_measured_item("medium nuggets", 5.0, -1, "side", 6, "nuggets")
	menu.add_measured_item("large nuggets", 7.0, -1, "side", 10, "nuggets") 
	menu.add_base_item("fries", 0, 6000, "side", ["small fries", "medium fries", "large fries"])
	set_quantity("fries")
	menu.add_measured_item("small fries", 2.5, -1, "side", 75, "fries")
	menu.add_measured_item("medium fries", 3.5, -1, "side", 150, "fries")
	menu.add_measured_item("large fries", 4.5, -1, "side", 250, "fries")
			
	#add drinks 
	menu.add_menu_item("water", 3.0, 1000, "drink") 
	menu.add_base_item("orange juice", 0, 10000, "drink", ["small orange juice", "medium orange juice",  "large orange juice"])
	set_quantity("orange juice")
	menu.add_measured_item("small orange juice", 2.5, -1, "drink", 250, "orange juice") 
	menu.add_measured_item("medium orange juice", 3.5,  -1, "drink", 450, "orange juice")
	menu.add_measured_item("large orange juice", 4.5, -1, "drink", 650, "orange juice")
	
	#add sundaes
	menu.add_base_item("sundae", 0, 10000, "dessert", ["small chocolate sundae", "medium chocolate sundae", "large chocolate sundae", "small strawberry sundae", "medium strawberry sundae", "large strawberry sundae"])
	set_quantity("sundae")
	menu.add_measured_item("small chocolate sundae", 3.5, -1, "drink", 250, "sundae") 
	menu.add_measured_item("medium chocolate sundae", 4.5, -1, "drink", 450, "sundae") 
	menu.add_measured_item("large chocolate sundae", 5.5, -1, "drink", 650, "sundae") 
	
	menu.add_measured_item("small strawberry sundae", 3.5, -1, "drink", 250, "sundae") 	
	menu.add_measured_item("medium strawberry sundae", 4.5, -1, "drink", 450, "sundae")
	menu.add_measured_item("large strawberry sundae", 5.5, -1, "drink", 650, "sundae") 
									
	return menu
