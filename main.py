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

  baseOp = prs.parseBase(command)
  trigOp = prs.parseTrig(command)

  if baseOp[0] == 'q\n':
    break
  if baseOp[1] == '+':
    print (calc.plus(float(baseOp[0]), float(baseOp[2])))
  if baseOp[1] == '-':
    print (calc.minus(float(baseOp[0]), float(baseOp[2])))
  if baseOp[1] == '*':
    print (calc.multiply(float(baseOp[0]), float(baseOp[2])))
  if baseOp[1] == '/':
    print (calc.divide(float(baseOp[0]), float(baseOp[2])))