from menuItem import *
import copy

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._items = {
		"burger": Main("burger", 0.0, 1000, "main"), 
		"wrap": Main("wrap", 0.0, 1000, "main"), 
		"sesame_bun": Ingredient("sesame_bun", 1.00, 1000, "bun"), 
		"muffin_bun": Ingredient("muffin_bun", 1.50, 1000, "bun"), 
		"beef_patty": Ingredient("beef_patty", 1.5, 1000, "patty"), 
		"veg_patty": Ingredient("veg_patty", 1, 1000, "patty"), 
		"white_wrap": Ingredient("white_wrap", 1.00, 1000, "wrap"), 
		"wholemal_wrap": Ingredient("wholemeal_wrap", 1.00, 1000, "wrap"), 
		"tuna_filling": Ingredient("tuna_filling", 1.5, 1000, "filling"), 
		"veg_filling": Ingredient("veg_filling", 1.5, 1000, "filling"), 
		"tomato": Ingredient("tomato", 0.5, 1000, "ingredient"), 
		"lettuce": Ingredient("lettuce", 0.5, 1000, "ingredient"), 
		"swiss_cheese": Ingredient("swiss_cheese", 0.5, 1000, "ingredient"), 
		"cheddar_cheese": Ingredient("cheddar_cheese", 0.5, 1000, "ingredient"), 
		"tomato_sauce": Ingredient("tomato_sauce", 0.5, 1000, "ingredient"), 
		"ians_special_sauce": Ingredient("ians_special_sauce", 3.0, 1000, "ingredient"), 
		"small_nuggets": Nugget("small_nuggets", 3.0, 10000/3, "side", 3), 
		"medium_nuggets": Nugget("medium_nuggets", 5.0, 10000/6, "side", 6), 
		"small_fries": Fries("small_fries", 2.5, 10000/75, "side", 75), 
		"medium_fries": Fries("medium_fries", 3.5, 10000/150, "side", 150), 
		"water": MenuItem("water", 3.0, 1000, "drink"), 
		"small_orange_juice": OrangeJuice("small_orange_juice", 2.0, 10000/250, "drink", 250), 
		"medium_orange_juice": OrangeJuice("medium_orange_juice", 3.5, 10000/450, "drink", 450)}
		self._unavailable = []
		
		
	#return copy of item on menu to place in order	
	def get_copy(self, name, quantity):
		newCopy = copy.deepcopy(self._items[name])
		newCopy.set_quantity(quantity)
		return newCopy
	
	def update_unavailable():
		pass
	
	#function to decrement inventory levels after an order is placed		
	def dec_inventory(self, items):
		for item in items:
			name = item.get_name()
			#decrement ingredients in a main item
			if(item.get_type() == "main"):
				ingredients = item.get_ingredients()
				for ingredient in ingredients:
					previous_quantity = self._items[ingredient.get_name()].get_quantity()
					order_quantity = ingredient.get_quantity()
					new_quantity = previous_quantity - order_quantity
					if(new_quantity < 1):
						self._unavailable.append(ingredient.get_name())
					self._items[ingredient.get_name()].set_quantity(new_quantity)
			#decrement side and drink (measured) items
			elif(name == "small_nuggets" or name == "medium_nuggets" or name == "small_fries" or name == "medium_fries" or name == "small_orange_juice" or name == "medium_orange_juice"):
				new_quantity = 0
				#case for nuggets	
				if(name == "small_nuggets" or name == "medium_nuggets"):
					previous_quantity = item.get_total_nuggets()
					order_quantity = item.get_quantity() * item.get_serving_size()
					new_quantity = previous_quantity - order_quantity
					item.set_total_nuggets(new_quantity)
					self._items["small_nuggets"].set_quantity(new_quantity/3)
					self._items["medium_nuggets"].set_quantity(new_quantity/6)
				#case for fries
				elif(name == "small_fries" or name == "medium_fries"): 
					previous_quantity = item.get_total_fries()
					order_quantity = item.get_quantity() * item.get_serving_size()
					new_quantity = previous_quantity - order_quantity
					item.set_total_fries(new_quantity)
					self._items["small_fries"].set_quantity(new_quantity/75)
					self._items["medium_fries"].set_quantity(new_quantity/150)
				#case for orange juice
				else: 
					previous_quantity = item.get_total_orange_juice()
					order_quantity = item.get_quantity() * item.get_serving_size()
					new_quantity = previous_quantity - order_quantity
					item.set_total_orange_juice(new_quantity)
					self._items["small_orange_juice"].set_quantity(new_quantity/250)
					self._items["medium_orange_juice"].set_quantity(new_quantity/450)
					
				if(new_quantity < 1):
					self._unavailable.append(name)
			#whatever menu items that is not a main or side or drink
			else: 
				previous_quantity = self._items[name]
				order_quantity = item.get_quantity()
				new_quantity = previous_quantity - order_quantity
				self._item[name].set_quantity(new_quantity)
				if(new_quantity < 1):
					self._unavailable.append(name)
		return		 
	
	#function to check whether we have enough stock to fulfil an order	
	def check_enough_inventory(self, items):
		not_enough = []
		for item in items:
			if(item.get_type() == "main"):
				ingredients = item.get_ingredients()
				for ingredient in ingredients:
					name = ingredient.get_name()
					if(ingredient.get_quantity() > self._items[name].get_quantity()):
						not_enough.append(name)
			else:
				name = item.get_name()
				if(item.get_quantity() > self._items[name].get_quantity()):
					not_enough.append(name)
		return not_enough
		
			
	def add_unavailable():
		pass
	
	def remove_unavailable():
		pass 
		
	def show_menu(self):
		for key in self._items:
			print(key)
		return	
		
	def show_inventory(self):
		for key in self._items:
			print("{0}: {1}".format(key, self._items[key].get_quantity()))	
		
	#modified print output	
	def __str__(self):
		for key in self._items:
			print("{0}: {1}".format(key, self._items[key]))
		return


