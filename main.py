import calculator
import parser
import input_output
import sys

inp = input_output.InputOutput()
prs = parser.Parser()
calc = calculator.Calculator('base')

calcType = sys.stdin.readline().rstrip()

while True:
  try:
    command = inp.get_input()
  except (IOError, KeyboardInterrupt):
    print '\nReturning to main menu...'

  if calcType == 'base':
    baseOp = prs.parseBase(command)
    if baseOp[0] == 'q':
      break
    if baseOp[1] == '+':
      print (calc.plus(float(baseOp[0]), float(baseOp[2])))
    if baseOp[1] == '-':
      print (calc.minus(float(baseOp[0]), float(baseOp[2])))
    if baseOp[1] == '*':
      print (calc.multiply(float(baseOp[0]), float(baseOp[2])))
    if baseOp[1] == '/':
      print (calc.divide(float(baseOp[0]), float(baseOp[2])))

  print(calcType)
  if calcType == 'trig':
    trigOp = prs.parseTrig(command)

    if trigOp[0] == 'q\n':
      break 
    if trigOp[0] == 'sin':
      print(calc.sin(float(trigOp[1])))