# exception handling for Gourmet burger systems

class OrderErrors(Exception):
    def __ init__(self,errors, msg=None):
        if msg is None:
            msg = "Order validation error occurred"
        super().__init__(msg)
        self.errors = errors

def check_order_error():
    errors = {}

    if 



    if errors:
        raise BookingError(errors)
