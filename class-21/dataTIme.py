from datetime import datetime , time , timezone , timedelta

print(datetime.now())

# print(time(hour=22, minute=10))

# print(datetime.now(timezone.utc))

result = datetime.now() + timedelta(days= - 7)

print(result)

format = "%d - %m"

print(datetime.now().strftime(format))