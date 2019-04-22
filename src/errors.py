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


def check_main_item_error(item):
    return None

def check_quantity_error(item):
    return
