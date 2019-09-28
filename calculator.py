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
    return '1'