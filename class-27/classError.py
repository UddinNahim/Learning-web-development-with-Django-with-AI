class CustomerError(Exception):
    
    def __init__(self, message ):
        self.message = message

        super().__init__(self.message)
try:
    raise CustomerError("This is a customer error message")
except CustomerError as e:
    print(e)



