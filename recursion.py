# Recursion
# A function calling itself

# Function Factorial
def getFactorial(n):
  if n == 1 : return 1
  return n * getFactorial(n - 1)

print(getFactorial(3))