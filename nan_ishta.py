import sys
import INTERPRETER

f = open(sys.argv[1], 'r')

for x in f:
    INTERPRETER.runCMD(x[:len(x)],isShell=False)
