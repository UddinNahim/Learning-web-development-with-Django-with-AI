from enum import Enum
class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3
    CANCELLED = 4

order_status = 3

if order_status == OrderStatus.PENDING.value:
    print('pending')
elif order_status == OrderStatus.PROCESSING.value:
    print("processing")
elif order_status == OrderStatus.COMPLETED.value:
    print("Completed")
else:
    print("no order")