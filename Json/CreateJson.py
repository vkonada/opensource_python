#Convert from Json to Python
import json
# some JSON:
x =  '{ "name":"Mark", "age":30, "city":"New Jersey"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON:
import json
# a Python object (dict):
x = {
  "name": "Mark",
  "age": 30,
  "city": "New Jersey"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''

#json data types
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

