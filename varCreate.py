# import re
import _core as c
import expression_exec as ex
import varcls

def checkName(name):
    validString = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_$"
    for x in name:
        # ind = validString.index(x)
        # print(ind)
        if x in validString:
            continue
        else:
            return False
    return True
        
def exe(modifier, variableName, value):

    if checkName(variableName) == False:
        print(f"NaamaDosha: \"{variableName}\" sariyaada hesaru alla.")
        return 0
    elif variableName in c.keywords:
        print(f"NaamaDosha: \"{variableName}\" nondaayita pada, addarinda hesarakkaagi prayoga madabaaradu.")
        return 0

    if modifier == 'SANKHYE':
        try:
            if value[0] == '"' or value[0] == "'":
                print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                return 0

            expression = ex.makeExp(value)
            # print(f"'{expression}'")
            c._variables[variableName] = varcls.Variable("SANKHYE", int(eval(expression)))
        except ValueError:
            if value in c._variables:
                c._variables[variableName] = varcls.Variable("SANKHYE", c._variables[value].value)
            else:
                print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                return 0

    elif modifier == 'SHABDA':
        if value[0] == "'":
            valueList = value[1:len(value)-1]
            value = ''
            for x in valueList:
                value += x
            c._variables[variableName] = value
        else:
            if value in c._variables:
                c._variables[variableName] = c._variables[value]

    elif modifier == 'DASHAMANSHA':
        try:
            if value[0] == '"' or value[0] == "'":
                print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                return 0

            expression = ex.makeExp(value)
            # print(f"'{expression}'")
            c._variables[variableName] = varcls.Variable("DASHAMANSHA", float(eval(expression)))
        except ValueError:
            if value in c._variables:
                c._variables[variableName] = varcls.Variable("DASHAMANSHA", c._variables[value].value)
            else:
                print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                return 0

    elif modifier == 'TARKA':
        try:
            if value[0] == '"' or value[0] == "'":
                print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
                return 0

            if value == 'SARI':
                c._variables[variableName] = varcls.Variable("TARKA", True)
            elif value == 'TAPPU':
                c._variables[variableName] = varcls.Variable("TARKA", False)
            else:
                expression = ex.makeExp(value)
                c._variables[variableName] = varcls.Variable("TARKA", bool(eval(expression)))
        except ValueError:
            print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
            return 0

    return f"{variableName} = {c._variables[variableName].value}"


'''
while True:
    statement = input("Enter a statement: ")

    # print(statement=='exit')
    if statement == 'exit':
        break

    answer = exe(statement)
    if answer==0:
        continue
    else:
        print(answer)
'''
