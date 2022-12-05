import _core as c
import expression_exec as ex
import math
import random

def makeStr(value):
    finalString = f" "
    varList = ''
    varName = ''
    isVar = False
    count = 0
    hasVar = False
    for x in value:
        if x == '{':
            isVar = True
            hasVar = True
            finalString += '{'
        elif x == '}':
            isVar = False
            finalString += f"{count}}}"
            varList += ex.makeExp(varName) + ', '
            # varList += "c._variables[\'"
            # varList += varName
            # varList += "\'].value, "
            varName =''
            count += 1
        else:
            if isVar:
                varName += x
            else:
                finalString += x

    finalString = finalString.strip()
    n = len(varList)
    if hasVar:
        final = f"{finalString}.format({varList[:n]})"
    else:
        final = finalString
    # print(final)
    return eval(final)
