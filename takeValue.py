import _core as c
import expression_exec as ex

def exe(isShell, varName, message):
    # print(varName, message)
    
    if varName in c._variables:
        inputVal = input(str(message[1:len(message)-1]))

        if c._variables[varName].datatype == 'SANKHYE':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" SANKHYE moulya alla.")
                    return 0

                expression = ex.makeExp(inputVal)
                c._variables[varName].value = int(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" SANKHYE moulya alla.")
                return 0
        
        elif c._variables[varName].datatype == 'DASHAMANSHA':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" DASHAMANSHA moulya alla.")
                    return 0

                expression = ex.makeExp(inputVal)
                c._variables[varName].value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" DASHAMANSHA moulya alla.")
                return 0

        elif c._variables[varName].datatype == 'TARKA':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" TARKA moulya alla.")
                    return 0

                if inputVal == 'SARI':
                    c._variables[varName].value = True
                elif inputVal == 'TAPPU':
                    c._variables[varName].value = False
                else:
                    expression = ex.makeExp(inputVal)
                    c._variables[varName].value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" TARKA moulya alla.")
                return 0

    else:
        print(f"AstitvaDosha: {varName} hesurina astitva illa.")
        return 0

    if isShell:
        print(f"{varName} = {c._variables[varName].value}")