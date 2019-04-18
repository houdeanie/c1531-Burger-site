from item import MenuItem, MainMenuItem, MeasuredMenuItem, BaseMenuItem, MainOrderItem

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._items = {}
	
	#functions to add items to the menu	
	def add_main(self, name, price, stock_quantity, food_type, ingredients):
		self._items[name] = MainMenuItem(name, price, stock_quantity, food_type, ingredients)	

	def add_measured_item(self, name, price, stock_quantity, food_type, serving_size, base_item):
		self._items[name] = MeasuredMenuItem(name, price, stock_quantity, food_type, serving_size, base_item)	     
        
	def add_menu_item(self, name, price, stock_quantity, food_type):
		self._items[name] = MenuItem(name, price, stock_quantity, food_type)  
    
	def add_base_item(self, name, price, stock_quantity, food_type, related_items):
		self._items[name] = BaseMenuItem(name, price, stock_quantity, food_type, related_items)
        
    #function to set the quantity of measured items from base items	 e.g. set quantity of "small nuggets", "medium nuggets" and "large nuggets" from "nuggets". base_item is a str
	def set_quantity(self, base_item):
		#not an item on the menu
		if not base_item in self._items:
			return False	
		#not a BaseMenuIte	
		if not isinstance(self._items[base_item], BaseMenuItem):
			return False
		related_items = self._items[base_item].related_items	
		total_quantity = self._items[base_item].stock_quantity	
		for item in related_items:
			serving_size = self._items[item].serving_size
			new_quantity = total_quantity / serving_size
			#if new quantity is < 1, new quantity = 0
			if new_quantity < 1:
				new_quantity = 0
			self._items[item].stock_quantity = new_quantity
		return True    

	#function to decrement stock quantity after an order is placed. items is a list of strings and MainOrderItems
	def dec_inventory(self, items):
		for item in items:
			if isinstance(item, MainOrderItem):
				ingredients = item.ingredients
				for ingredient in ingredients:
					self._items[ingredient].stock_quantity -= 1
			elif isinstance(item, MenuItem):
				self._items[item].stock_quantity -= 1
			elif isinstance(item, MeasuredMenuItem):
				base_item = self._items[item].base_item
				serving_size = self._items[item].serving_size
				self._items[base_item].stock_quantity -= serving_size
				set_quantity(base_item)
		return	

	#function to check whether we have enough stock to fulfil an order. items is a list of strings and MainOrderItems
	def check_enough_inventory(self, items):
		insufficient = {}
		for item in items:
			#if main item, we check its ingredients against stock levels
			if isinstance(item, MainOrderItem):
				ingredients = item.ingredients
				for ingredient in ingredients:
					count = ingredients.count(ingredient) 
					if count > self._items[ingredient].stock_quantity:
						insufficient[ingredient] = self._items[ingredient].stock_quantity
			else:
				if items.count(item) > self._items[item].stock_quantity:
					insufficient[item] = self._items[item].stock_quantity
		return insufficient

	#function to set the quantity of base wrap and base burger based on the least available ingredient
	def set_main_quantity(self, main_item):
		ingredients = self.get_item(main_item).ingredients
		quantity = self.get_stock_quantity(ingredients[0])
		for ingredient in ingredients:
			count = ingredients.count(ingredient)
			if (self.get_stock_quantity(ingredient) / count) < quantity:
				quantity = self.get_stock_quantity(ingredient) / count
		self.set_stock_quantity(main_item, quantity)
		return

	def display(self):
		return self._items.values()
    	
	def print_menu(self):
		for item in self._items.keys():
			print(self.get_item(item))
    		   		
	def get_item(self, name):
		return self._items[name]     
    	
	def get_items(self):
		return self._items
		
	#function that returns the quantity of an item in string format
	def get_stock_quantity(self, name):
		quantity = self.get_item(name).stock_quantity
		return quantity

	#function that sets the quantity of an item in string format
	def set_stock_quantity(self, name, quantity):
		self.get_item(name).stock_quantity = quantity
		return 
		
	#function to refill inventory to full
	def refill_inventory(self):
		for item in self._items.keys():
			if self.get_item(item).food_type == "ingredient":
				self.set_stock_quantity(item, 1000)
			elif isinstance(self.get_item(item), BaseMenuItem):
				self.set_stock_quantity(item, 10000)
		self.set_main_quantity("baseburger")
		self.set_main_quantity("base wrap")		
		self.set_quantity("nugget")
		self.set_quantity("fries")
		self.set_quantity("orange juice")
		self.set_quantity("sundae")
		return
		
	#function to return a list of mains on the menu only
	def get_mains(self):
		mains = []
		for item in self._items.keys():
			if self.get_item(item).food_type == "main":
				mains.append(self.get_item(item))
		return mains
	
	#function to return a list of ingredients on the menu only
	def get_ingredients(self):
		ingredients = []
		for item in self._item.keys():
			if self.get_item(item).food_type == "ingredient":
				ingredients.append(self.get_item(item))
		return ingredients
	
	#function to return a list of sides on the menu only
	def get_sides(self):
		sides = []
		for item in self._item.keys():
			if self.get_item(item).food_type == "side" and not isinstance(self.get_item(item), BaseMenuItem):
				sides.append(self.get_item(item))
		return sides	
	
	#function to return a list of drinks on the menu only
	def get_drinks(self):
		drinks = []
		for item in self._item.keys():
			if self.get_item(item).food_type == "drink" and not isinstance(self.get_item(item), BaseMenuItem):
				drinks.append(self.get_item(item))
		return drinks	
	
	#function to return a list of sundaes on the menu only
	def get_desserts(self):
		desserts = []
		for item in self._item.keys():
			if self.get_item(item).food_type == "dessert" and not isinstance(self.get_item(item), BaseMenuItem):
				desserts.append(self.get_item(item))
		return desserts			
