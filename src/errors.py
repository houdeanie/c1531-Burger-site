# exception handling for Gourmet burger systems

class OrderError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Order validation error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg)
        self.errors = errors

# check for order problems
def check_order_error(order):
    errors = {}
    
    # empty order
    if order._items == []:
        errors['empty_order'] = "Must have at least one item in the order"
    
    # an item in the order doesn't have any ingredients
    no_ingred = False
    for item in order._items:
        if item.get_type() == "main":
            if item.get_ingredients() == []:
                no_ingred = True
    if no_ingred == True:
        errors['ingredients'] = "Item must have at least one ingredient"

    if errors:
        raise OrderError(errors)

# checks if burger or wrap is valid given preconditions
def check_main_error(item, type):
    errors = []
    # burger must have 2 - 3 buns
    # burger must have no more than 3 patties
    # wrap must have at least 1 wrap
    if type == 'burger':
        total = {'bun': 0, 'patty': 0}
        for key, value in item.ingredients.items():
            ing = system.display_item(key)
            if ing.ing_type == 'bun':
                total['bun']  += value
            if ing.ing_type == 'patty':
                total['patty'] += value
        if total['bun'] < 2 or total['bun'] > 4:
            errors.append('Total buns must be more than or equal to 2 and less than or equal to 4')
        if total['patty'] > 3:
            errors.append('Total patties ust be less than or equal to 3')
        if len(errors) != 0:
            return errors
    elif type == 'wrap':
        ing = item.ingredients
        total = {'wrap': 0}
        for key, value in item.ingredients.items():
            ing = system.display_item(key)
            if ing.ing_type == 'wrap':
                total['wrap']  += value
        if total['wrap'] != 1:
            errors.append('Total wraps must be 1')
        if len(errors) != 0:
            return errors
    return None

def check_quantity_error(item):
    return
