from menuItem import MenuItem, Main, MeasuredItem, BaseItem

#class to represent the Menu and Inventory
class Menu:
	def __init__(self):
		self._items = {}
	
	#functions to add items to the menu	
	def add_main(self, name, price, stock_quantity, food_type, ingredients):
		self._items[name] = Main(name, price, stock_quantity, food_type, ingredients)	

	def add_measured_item(self, name, price, stock_quantity, food_type, serving_size, base_item):
		self._items[name] = MeasuredItem(name, price, stock_quantity, food_type, serving_size, base_item)	     
        
	def add_menu_item(self, name, price, stock_quantity, food_type):
		self._items[name] = MenuItem(name, price, stock_quantity, food_type)  
    
	def add_base_item(self, name, price, stock_quantity, food_type, related_items):
		self._items[name] = BaseItem(name, price, stock_quantity, food_type, related_items)
        
	def display(self):
		return self._items.values()
    	
	def print_menu(self):
		for item in self._items.keys():
			print(self.get_item(item))
    		   		
	def get_item(self, name):
		return self._items[name]     
    	
    #function to set the quantity of measured items from base items	
	def set_quantity(self, base_item):
		if not base_item in self._items:
			return False	
		if not isinstance(self._items[base_item], BaseItem):
			return False
		related_items = self._items[base_item].related_items	
		total_quantity = self._items[base_item].stock_quantity	
		for item in related_items:
			serving_size = self._items[item].serving_size
			new_quantity = total_quantity / serving_size
			if new_quantity < 1:
				new_quantity = 0
			self._items[item].stock_quantity = new_quantity
		return True    

	#function to decrement stock quantity after an order is placed
	def dec_inventory(self, items):
		for item in items:
			if isinstance(item, Main):
				ingredients = item.ingredients
				for ingredient in ingredients:
					self._items[ingredient].stock_quantity -= 1
			elif isinstance(item, MenuItem):
				self._items[item].stock_quantity -= 1
			elif isinstance(item, MeasuredItem):
				base_item = self._items[item].base_item
				serving_size = self._items[item].serving_size
				self._items[base_item].stock_quantity -= serving_size
				set_quantity(base_item)
		return	

	#function to check whether we have enough stock to fulfil an order					
	def check_enough_inventory(self, items):
		insufficient = {}
		for item in items:
			if(item.food_type == "main"):
				ingredients = item.ingredients
				for ingredient in ingredients:
					count = ingredients.count(ingredient) 
					if count > self._items[ingredient].stock_quantity:
						insufficient[ingredient] = self._items[ingredient].stock_quantity:
			else:
				if items.count(item) > self._items[item].stock_quantity:
					insufficient[item] = self._items[item].stock_quantity
		return insufficient


