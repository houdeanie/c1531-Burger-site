import menuItem

#testing menuItem	
tomato = menuItem.Ingredient("tomato", 0.5, 1000, "ingredient")
print(tomato)
beef_patty = menuItem.Ingredient("beef_patty", 2, 2000, "patty")
tomato = menuItem.Ingredient("tomato", 0.5, 1000, "ingredient")
lettuce = menuItem.Ingredient("lettuce", 0.5, 1000, "ingredient")
cheese = menuItem.Ingredient("cheese", 0.5, 1000, "ingredient")


burger = menuItem.Main("burger", 3.0, 1, "main")
print(burger)	
burger.add_ingredient(tomato)
print(burger)	
burger.add_ingredient(beef_patty)
print(burger)	
burger.add_ingredient(lettuce)
print(burger)	
	
