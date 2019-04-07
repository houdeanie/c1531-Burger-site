# exception handling for Gourmet burger systems

class OrderError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Order validation error occurred with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg)
        self.errors = errors

def check_order_error(order):
    errors = {}
    
    # empty order
    if len(order.items) == 0:
        errors['empty_order'] = "Must have at least one item in the order"
    
    # invalid order due to inventory



    if errors:
        raise BookingError(errors)
