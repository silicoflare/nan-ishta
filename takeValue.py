import _core as c
import expression_exec as ex

def exe(varName, message):
    if varName in c._variables:
        inputVal = input(str(message[1:len(message)-1]))

        variableRef =  c._variables[varName]
        if variableRef.datatype == 'SANKHYE':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" SANKHYE moulya alla.")
                    return 0

                expression = ex.makeExp(inputVal)
                variableRef.inputVal = int(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" SANKHYE moulya alla.")
                return 0
        
        elif variableRef.datatype == 'DASHAMANSHA':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" DASHAMANSHA moulya alla.")
                    return 0

                expression = ex.makeExp(inputVal)
                variableRef.inputVal = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" DASHAMANSHA moulya alla.")
                return 0

        elif variableRef.datatype == 'TARKA':
            try:
                if inputVal[0] == '"' or inputVal[0] == "'":
                    print(f"MoulyaDosha: \"{inputVal}\" TARKA moulya alla.")
                    return 0

                if inputVal == 'SARI':
                    variableRef.inputVal = True
                elif inputVal == 'TAPPU':
                    variableRef.inputVal = False
                else:
                    expression = ex.makeExp(inputVal)
                    variableRef.inputVal = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{inputVal}\" TARKA moulya alla.")
                return 0

    else:
        print(f"AstitvaDosha: {varName} hesurina astitva illa.")
        return 0

    print(f"{varName} = {c._variables[varName].inputVal}")