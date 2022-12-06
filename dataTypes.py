# Most common data types
# LIST
items = ["roger", "1", "True", "syd", "quincy", '7']

dogs_partial = items[2:4]
dogs_partial.append("judah")

items.extend(dogs_partial)
items.remove("syd")

last_item = items.pop()
items.insert(0, last_item)

sorted_items = items[:]

# TUPLES
names = ("Roger", "Syd", "Beau")
#print("Kevin" in names)

#print(sorted(names, key=str.lower))

new_tuple = names + ("Tina", "Quincy")
#print(new_tuple)

# DICTIONARIES
dog = {"name": "Roger", "age": 29, "color": "green"}
dog["name"] = "Syd"
#print(dog.keys())

keys_list = list(dog.keys())
values_list = list(dog.values())
items_list = list(dog.items())
dog_color = dog.pop("color")
last_value = dog.popitem()

# print("color" in dog)

dog["food"] = "salmon"

del dog["food"] # deletes food property from dictionary

dog_copy = dog.copy()

# SETS
# sets don't have keys just values
# sets are not ordered
# Sets don't have duplicate values

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersept = set1 & set2  #gets the common values
union = set1 | set2  # combines both sets into one with not repeated values
difference = set1 - set2  #gets the different value(s)

# check if a set is subset of the other
# using ">" it verifies if the set on the left has all the values from the set of the right
subset = set1 > set2  # prints Ture

# get list from set
list1 = list(set1)

# print("Roger" in list1)