from typing import Dict

def process_entity(person: Dict):
    if person['salary'] < 5000:
        raise ValueError("salary too low")
    cal = person['salary'] / person['tax']
    return cal

p = {
    "salary" : 1000,
    "tax" : 0
}


try:
    val = process_entity(person=p)
    print(val)
except ZeroDivisionError as e:
    print("ZerodivisionError", e)

except KeyError as e:
    print("Key not found", e)

except Exception as e:
    print(e)
except ValueError as e:
    print(e)