class Calculator:

  def __init__(self, name):
    self.name = name

  def change_name(self, new_name):
    self.name = new_name


  def plus(self, a, b):
    return a + b

  def minus(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    return a / b
