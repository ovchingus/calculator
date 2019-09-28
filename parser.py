class Parser:
  """Contains custom user input parser
  """

  def parseBase(self, string):
    """Parse user input for simple operations
    
    Arguments:
        string {str} -- [description]
    
    Returns:
        [str] -- Array of strings with numbers and sign
        Example: ['1', '+', '12']
    """
    arr = string.split(' ')
    return arr

  def parseTrig(self, string):
    op = string.split('(')[0]
    num = string.split('(')[1].split(')')[0]
    return [op, num]