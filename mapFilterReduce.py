# Global functions to work with collections
from functools import reduce

# -- map() --
numbers = [1, 2, 3]

# Using regular function
def double(a):
  return a * 2

# Using lambda function
doubleB = lambda a : a * 2

result = list(map(double, numbers))
print(result)

resultB = list(map(doubleB, numbers))
print(resultB)

# simplified using lamda
resultC = list(map(lambda a : a * 2, numbers))
print(resultC)

# -- filter() --
numbers.append(4)

# Using regular functions
def isEven(n):
  return n % 2 == 0

resultFilter = list(filter(isEven, numbers))
print(resultFilter)

# Using lambda function
isEvenB = lambda a : a % 2 == 0

resultFilterB = list(filter(isEvenB, numbers))
print(resultFilterB)

# simplified using lambda
resultFilterC = list(filter(lambda a : a % 2 == 0, numbers))
print(resultFilterC)

# -- reduce() -- 
# needs to be imported from functools

expenses = [
  ('Dinner', 80),
  ('Car Repair', 120)
]

sum = 0

# using for in loop
for expense in expenses:
  sum += expense[1]

print(sum)

# using reduce
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)