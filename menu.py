from menuItem import Main, Ingredient, MeasuredItem

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._mains = [Main("burger", 0.0, 1000, "main"), Main("wrap", 0.0, 1000, "main")]
		self._bun_types = [Ingredient("sesame_bun", 1.00, 1000, "bun"), Ingredient("muffin_bun", 1.50, 1000, "bun")]
		self._patty_types = [Ingredient("beef_patty", 1.5, 1000, "patty"), Ingredient("vegan_patty", 1, 1000, "patty")]
		self._wrap_types = [Ingredient("white_wrap", 1.00, 1000, "wrap"), Ingredient("wholemeal_wrap", 1.00, 1000, "wrap")]
		self._filling_types = [Ingredient("tuna_filling", 1.5, 1000, "filling"), Ingredient("vegan_filling", 1.5, 1000, "filling")] 
		self._ingredients = [Ingredient("tomato", 0.5, 1000, "ingredient"), Ingredient("lettuce", 0.5, 1000, "ingredient"), Ingredient("swiss_cheese", 0.5, 1000, "ingredient"), Ingredient("cheddar_cheese", 0.5, 1000, "ingredient"), Ingredient("tomato_sauce", 0.5, 1000, "ingredient"), Ingredient("ians_special_sauce", 3.0, 1000, "ingredient")]
		self._sides = [MeasuredItem("small_nuggets", 3.0, 1000, "side", 3), MeasuredItem("medium_nuggets", 5.0, 1000, "side", 6), MeasuredItem("small_fries", 2.5, 1000, "side", 75), MeasuredItem("medium_fries", 3.5, 1000, "side", 125), MeasuredItem("large_fries", 5, 1000, "side", 200)]
		self._drinks = [MeasuredItem("water", 3.0, 1000, "drink", 600), MeasuredItem("small_orange_juice", 2.0, 1000, "drink", 250), MeasuredItem("medium_orange_juice", 3.5, 1000, "drink", 450)]
		self._unavailable = []
		
	def update_unavailable():
		pass
	
	#function to decrement inventory levels after an order is placed		
	def dec_inventory(self, items):
		for item in items:
			if(item.get_type == "main"):
				ingredients = item.get_ingredients()
				for ingredient in ingredients:
					if(ingredient.get_type() == "bun"):
						for bun in self._bun_types:
							if(ingredient.get_name() == bun.get_name()):
								ingredient.set_quantity(ingredient.get_quantity() - 1)
					elif(ingredient.get_type() == "patty"):
						for patty in self._patty_types:
							if(ingredient.get_name() == patty.get_name()):
								ingredient.set_quantity(ingredient.get_quantity() - 1)
					elif(ingredient.get_type() == "wrap"):
						for wrap in self._wrap_types:
							if(ingredient.get_name() == wrap.get_name()):
								ingredient.set_quantity(ingredient.get_quantity() - 1) 
					elif(ingredient.get_type() == "filling"):
						for filling in self._filling_types:
							if(ingredient.get_name() == filling.get_name()):
								ingredient.set_quantity(ingredient.get_quantity() - 1)
					elif(ingredient.get_type() == "ingredient"):
						for ing in self._ingredients:
							if(ingredient.get_name() == ing.get_name()):
								ingredients.set_quantity(ingredient.get_quantity() -1)  
			elif(item.get_type == "side"):
				if(item.get_name() == "small_nuggets" OR item.get_name() == "medium_nuggets"):
					for side in self._sides:
						if(side.get_name() == "small_nuggets" OR side.get_name() == "medium_nuggets"):
							side.set_quantity(side.get_quantity() - item.get_serving_size())
				elif(item.get_name() == "small_fries" OR item.get_name() == "medium_fries" OR item.get_name() == "large_fries"):
					for side in self._sides:
						if(side.get_name() == "small_fries" OR side.get_name() == "medium_fries" OR side.get_name() == "large_fries"):
							side.set_quantity(side.get_quantity() - item.get_serving_size())
			else:
				if(item.get_name() == "water"):
					for drink in self.drinks:
						if(drink.get_name() == "water"):
							drink.set_quantity(drink.get_quantity() - item.get_serving_size())
				elif(item.get_name() == "small_orange_juice" OR item.get_name() == "medium_orange_juice"):
					for drink in self.drinks:
						if(drink.get_name() == "small_orange_juice" OR drink.get_name() == "medium_orange_juice"):
							drink.set_quantity(drink.get_quantity() - item.get_serving_size())
		return		 
		
	def add_unavailable():
		pass
	
	def remove_unavailable():
		pass 
	
	#modified print output	
	def __str__(self):
		return "mains: {0}, bun_types: {1}, patty_types: {2}, wrap_types: {3}, filling_types: {4}, ingredients: {5}, sides: {6}, drinks: {7}, unavailable: {8}".format(self._mains, self._bun_types, self._patty_types, self._wrap_types, self._filling_types, self._ingredients, self._sides, self._drinks, self._unavailable)
