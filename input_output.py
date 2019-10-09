import sys

class InputOutput:
  """Contains methods to controlinput and output operations
  """
  def get_input(self):
    """Custom input method
    
    Returns:
        str -- User input string
    """
    print('Operation: ')
    string = sys.stdin.readline()
    return string