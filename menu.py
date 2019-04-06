from menuItem import Main, Ingredient, MeasuredItem

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._mains = [Main("burger", 0.0, 1000, "main"), Main("wrap", 0.0, 1000, "main")]
		self._bun_types = [Ingredient("sesame_bun", 1.00, 1000, "ingredient"), Ingredient("muffin_bun", 1.50, 1000, "ingredient")]
		self._patty_types = [Ingredient("beef_patty", 1.5, 1000, "ingredient"), Ingredient("vegan_patty", 1, 1000, "ingredient")]
		self._wrap_types = [Ingredient("white_wrap", 1.00, 1000, "ingredient"), Ingredient("wholemeal_wrap", 1.00, 1000, "ingredient")]
		self._filling_types = [Ingredient("tuna_filling", 1.5, 1000, "ingredient"), Ingredient("vegan_filling", 1.5, 1000, "ingredient")] 
		self._ingredients = [Ingredient("tomato", 0.5, 1000, "ingredient"), Ingredient("lettuce", 0.5, 1000, "ingredient"), Ingredient("swiss_cheese", 0.5, 1000, "ingredient"), Ingredient("cheddar_cheese", 0.5, 1000, "ingredient"), Ingredient("tomato_sauce", 0.5, 1000, "ingredient"), Ingredient("ians_special_sauce", 3.0, 1000, "ingredient")]
		self._sides = [MeasuredItem("small_nuggets", 3.0, 1000, "side", 3), MeasuredItem("medium_nuggets", 5.0, 1000, "side", 6), MeasuredItem("small_fries", 2.5, 1000, "side", 75), MeasuredItem("medium_fries", 3.5, 1000, "side", 125), MeasuredItem("large_fries", 5, 1000, "side", 200)]
		self._drinks = [MeasuredItem("water", 3.0, 1000, "drink", 600), MeasuredItem("small_orange_juice", 2.0, 1000, "drink", 250), MeasuredItem("medium_orange_juice", 3.5, 1000, "drink", 450)]
		self._unavailable = []
		
	def update_unavailable():
		pass
			
	def dec_inventory():
		pass
		
	def add_unavailable():
		pass
	
	def remove_unavailable():
		pass 
	
	#modified print output	
	def __str__(self):
		return "mains: {0}, bun_types: {1}, patty_types: {2}, wrap_types: {3}, filling_types: {4}, ingredients: {5}, sides: {6}, drinks: {7}, unavailable: {8}".format(self._mains, self._bun_types, self._patty_types, self._wrap_types, self._filling_types, self._ingredients, self._sides, self._drinks, self._unavailable)
