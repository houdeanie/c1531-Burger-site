from menuItemSubClasses import *

def test_menuItemSubClasses():
#, name, price, quantity, type)
	sesame_bun = Ingredient("sesame_bun", 1, 2000, "bun")
	beef_patty = Ingredient("beef_patty", 2, 2000, "patty")
	tomato = Ingredient("tomato", 0.5, 1000, "ingredient")
	lettuce = Ingredient("lettuce", 0.5, 1000, "ingredient")
	cheese = Ingredient("cheese", 0.5, 1000, "ingredient")
	
	burger1 = Main("single_burger", -1, 1, "burger")
	assert(burger1.calc_price() == 0)	
	burger1.add_ingredient(sesame_bun)
	burger1.add_ingredient(sesame_bun)
	burger1.add_ingredient(beef_patty)
	burger1.add_ingredient(tomato)	
	burger1.add_ingredient(lettuce)
	burger1.add_ingredient(cheese)
	assert(burger1.calc_price() == 5.5)
