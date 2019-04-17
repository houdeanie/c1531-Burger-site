#parent class for all items offered by GourmetBurgers
class MenuItem:
	def __init__(self, name, price, stock_quantity, food_type):
		self._name = name
		self._price = price
		self._stock_quantity = stock_quantity
		self._food_type = food_type

	#getter and setter functions
	@property
	def name(self):
		return self._name
		
	@name.setter		
	def name(self, name):
		self._name = name
		
	@property		
	def price(self):
		return self._price
		
	@price.setter		
	def price(self, price):
		self._price = price

	@property		
	def stock_quantity(self):
		return self._stock_quantity

	@stock_quantity.setter		
	def stock_quantity(self, stock_quantity):
		self._stock_quantity = stock_quantity

	@property		
	def food_type(self):
		return self._food_type
		
	@food_type.setter		
	def food_type(self, food_type):
		self._food_type = food_type
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: ${1}, stock_quantity: {2}, food_type: {3}".format(self._name, self._price, self._stock_quantity, self._food_type)
		
#subclass for all mains 
class Main(MenuItem):
	def __init__(self, name, price, stock_quantity, food_type, ingredients):
		super().__init__(name, price, stock_quantity, food_type)
		self._ingredients = ingredients

	#getter functions
	@property	
	def ingredients(self):
		return self._ingredients[::]
		 
	#function to add ingredients 	
	def add_ingredient(self, ingredient):
		self._ingredients.append(ingredient)
		self._price += ingredient.price
		return
	
	#function to show ingredients
	def show_ingredients(self):
		if (len(self._ingredients) == 0):
			return "none"
		else:
			ingredients = []
			for x in self._ingredients:
				ingredients.append(x.get_stock_quantity())
				ingredients.append(x.get_name())

		return ingredients
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: ${1}, stock_quantity: {2}, food_type: {3}, ingredients: {4}".format(self._name, self._price, self._stock_quantity, self._food_type, self._ingredients)
		
#subclass for items that come in quantities != 1 and have different sizes e.g. (fries, nuggets, orange juice etc)
class MeasuredItem(MenuItem):
	def __init__(self, name, price, stock_quantity, food_type, serving_size, base_item):
		super().__init__(name, price, stock_quantity, food_type)
		self._serving_size = serving_size
		self._base_item = base_item
		
	#getter and setter functions
	@property
	def serving_size(self):
		return self._serving_size

	@serving_size.setter	
	def serving_size(self, size):
		self._serving_size = size
		
	@property
	def base_item(self):
		return self._base_item
		
	@base_item.setter
	def base_item(self, quantity):
		self._base_item = base_item			
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: {1}, stock_quantity: {2}, food_type: {3}, serving_size: {4}, pile_quantity: {5}".format(self._name, self._price, self._stock_quantity, self._food_type, self._serving_size, self._pile_quantity)
		
		
#subclass for items that are used to keep track of measured items e.g. total nuggets
class BaseItem(MenuItem):
	def __init__(self, name, price, stock_quantity, food_type, related_items):
		super().__init__(name, price, stock_quantity, food_type)
		self._related_items = related_items

	@property
	def related_items(self):
		return self._related_items[::]
		
	@related_items.setter
	def related_items(self, related_item):
		self._related_item = related_item

		
