from typing import Dict

def process_entity(person: Dict):
    cal = person['salary'] / person['tax']
    return cal

p = {
    "salary" : 1000,
    "tax" : 0
}


try:
    val = process_entity(person=p)
    print(val)
except Exception as e:
    print(e)

"""
in this code, there is a error for 0 , so we use try,exceptions.after the catching errror we can use ,"Exception" and print the error message
"""
    