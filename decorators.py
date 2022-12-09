# Decorators

def logtime(func):
  def wrapper():
    # Do something before
    val = func()
    # Do something after
    return val
  return wrapper

@logtime
def hello():
  print("Hello")

