from datetime import datetime

date_string = "21 June, 2025"

date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)
