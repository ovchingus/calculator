import calculator
import parser
import input_output

inp = input_output.InputOutput()
prs = parser.Parser()
calc = calculator.Calculator('base')

while True:
  try:
    command = inp.get_input()
  except (IOError, KeyboardInterrupt):
    print '\nReturning to main menu...'

  arr = prs.parseBase(command)

  if arr[0] == 'q\n':
    break
  if arr[1] == '+':
    print (calc.plus(float(arr[0]), float(arr[2])))
  if arr[1] == '-':
    print (calc.minus(float(arr[0]), float(arr[2])))
  if arr[1] == '*':
    print (calc.multiply(float(arr[0]), float(arr[2])))
  if arr[1] == '/':
    print (calc.divide(float(arr[0]), float(arr[2])))