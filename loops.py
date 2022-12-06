# LOOPS

# while loops
counter = 0
while counter < 3:
  print(counter + 1)
  counter += 1

# for in loop
items = [1, 2, 3, 4]
for index, item in enumerate(items):
  print(index, item)

# for in range loop
for item in range(15):
  print(item)

list_items = [1, 2, 3, 4]
for item in list_items:
  if item == 2:
    continue
  print(item)
