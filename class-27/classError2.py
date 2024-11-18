from typing import Dict
class DetailedError(Exception):
    
    def __init__(self, message ,code ):
        self.message = message
        self.code = code

        super().__init__(self.message)
try:
    raise DetailedError ("This is a customer error message" , 404)
except DetailedError as e:
    print( f"Error:, {e.message} (Code : {e.code})")



