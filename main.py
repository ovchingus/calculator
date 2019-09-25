import calculator
import parser
import input_output

inp = input_output.InputOutput()
prs = parser.Parser()
calc = calculator.Calculator('base')

while inp.get_input != 'q':
    try:
      command = inp.get_input()
    except (IOError, KeyboardInterrupt):
      print '\nReturning to main menu...'

    arr = prs.parse(command)

    if arr[1] == '+':
      print (calc.plus(float(arr[0]), float(arr[2])))
    if arr[1] == '-':
      print (calc.minus(float(arr[0]), float(arr[2])))
    if arr[1] == '*':
      print (calc.multiply(float(arr[0]), float(arr[2])))
    if arr[1] == '/':
      print (calc.divide(float(arr[0]), float(arr[2])))