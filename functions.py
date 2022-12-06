# FUNCTIONS
def hello(name="", age=0):
  print(f"Hello {name}! You are {age} years old!")


def change(value, new_name="syd"):
  value["name"] = new_name


val = {"name": "roger"}
change(val, "Josh")
# print(val) --> will change the dictionary to the new name we passed


def greet(name):
  if not name:
    return
  print(f"Hello {name}")
  return name, "Beau"


def talk(phrase):

  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)


def count():
  count = 0

  def increment():
    nonlocal count
    count += 1
    print(count)

  increment()


def counter():
  count = 0

  def increment():
    nonlocal count
    count += 1
    return count

  return increment


increment = counter()