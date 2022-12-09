# Docstrings

def increment(n):
  """Increment a number"""
  return n + 1

print(increment(3))

class Dog:
  """A class representing a dog"""
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def bark(self):
    """Let the dog bark"""
    print("Woof")

print(help(Dog))