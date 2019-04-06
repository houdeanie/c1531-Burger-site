from menuItem import Main, Ingredient, MeasuredItem

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._items = {"burger": Main("burger", 0.0, 1000, "main"), "wrap": Main("wrap", 0.0, 1000, "main"), "sesame_bun": Ingredient("sesame_bun", 1.00, 1000, "bun"), "muffin_bun": Ingredient("muffin_bun", 1.50, 1000, "bun"), "beef_patty": Ingredient("beef_patty", 1.5, 1000, "patty"), "veg_patty": Ingredient("veg_patty", 1, 1000, "patty"), "white_wrap": Ingredient("white_wrap", 1.00, 1000, "wrap"), "wholemal_wrap": Ingredient("wholemeal_wrap", 1.00, 1000, "wrap"), "tuna_filling": Ingredient("tuna_filling", 1.5, 1000, "filling"), "veg_filling": Ingredient("veg_filling", 1.5, 1000, "filling"), "tomato": Ingredient("tomato", 0.5, 1000, "ingredient"), "lettuce": Ingredient("lettuce", 0.5, 1000, "ingredient"), "swiss_cheese": Ingredient("swiss_cheese", 0.5, 1000, "ingredient"), "cheddar_cheese": Ingredient("cheddar_cheese", 0.5, 1000, "ingredient"), "tomato_sauce": Ingredient("tomato_sauce", 0.5, 1000, "ingredient"), "ians_special_sauce": Ingredient("ians_special_sauce", 3.0, 1000, "ingredient"), "small_nuggets": MeasuredItem("small_nuggets", 3.0, 1000, "side", 3), "medium_nuggets": MeasuredItem("medium_nuggets", 5.0, 1000, "side", 6), "small_fries": MeasuredItem("small_fries", 2.5, 1000, "side", 75), "medium_fries": MeasuredItem("medium_fries", 3.5, 1000, "side", 125), "large_fries": MeasuredItem("large_fries", 5, 1000, "side", 200), "water": MeasuredItem("water", 3.0, 1000, "drink", 600), "small_orange_juice": MeasuredItem("small_orange_juice", 2.0, 1000, "drink", 250), "medium_orange_juice": MeasuredItem("medium_orange_juice", 3.5, 1000, "drink", 450)}
		self._unavailable = {}
		
	def update_unavailable():
		pass
	
	#function to decrement inventory levels after an order is placed		
	def dec_inventory(self, items):
		for item in items:
			#decrement ingredients in a main item
			if(item.get_type == "main"):
				ingredients = item.get_ingredients()
				for ingredient in ingredients:
					self._items[ingredient.get_name()].set_quantity(self._items[ingredient.get_name()].get_quantity() - 1)
			#decrement side and drink items
			else:
				self._items[item].set_quantity(self._items[item].get_quantity() - 1) 
		return		 
		
	def add_unavailable():
		pass
	
	def remove_unavailable():
		pass 
