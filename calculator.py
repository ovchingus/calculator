import math

class Calculator:
  """Contains math methods for calculating values
  """

  def __init__(self, name):
    self.name = name

  def change_name(self, new_name):
    self.name = new_name
    

  def plus(self, a, b):
    """Return plus operation result
    
    Arguments:
        a {int} -- first argument
        b {int} -- second argument
    
    Returns:
        int -- result of sum
    """
    return a + b

  def minus(self, a, b):
    """Return minus operation result
    
    Arguments:
        a {int} -- first argument
        b {int} -- second argument
    
    Returns:
        int -- result of minus
    """
    return a - b

  def multiply(self, a, b):
    """Return multiply operation result
    
    Arguments:
        a {int} -- first argument
        b {int} -- second argument
    
    Returns:
        int -- result of multiply
    """
    return a * b

  def divide(self, a, b):
    """Return divide operation result
    
    Arguments:
        a {int} -- first argument
        b {int} -- second argument
    
    Returns:
        int -- result of divide
    """
    return a / b

  def sin(self, a):
    """Return sinus operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of sinus operation
    """
    return math.sin(a)

  def cos(self, a):
    """Return cosinus operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of cosinus operation
    """
    return math.cos(a)

  def tan(self, a):
    """Return tan operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of tan operation
    """
    return math.tan(a)

  def asin(self, a):
    """Return arcsin operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of arcsin operation
    """
    return math.asin(a)

  def acos(self, a):
    """Return arccos operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of arccos operation
    """
    return math.acos(a)

  def atan(self, a):
    """Return arctan operation result
    
    Arguments:
        a {int} -- angle in radians
    
    Returns:
        float -- result of arctan operation
    """
    return math.atan(a)