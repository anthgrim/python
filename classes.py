# CLASSES
class Animal:
  def walk(self):
    print("walking")

class Dog(Animal):
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # method. Always pass "self"
  def bark(self):
    print("woof!")
  
  def identify(self):
    identification = {"name": self.name, "age": self.age}
    print(identification)

roger = Dog("Roger", 25)
roger.bark()
roger.identify()
roger.walk()
print(type(roger))