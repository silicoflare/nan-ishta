import _core as c
import expression_exec as ex

def exe(varName, value):
    if varName in c._variables:
        variableRef =  c._variables[varName]
        if variableRef.datatype == 'SANKHYE':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                    return 0

                expression = ex.makeExp(value)
                variableRef.value = int(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                return 0
        
        elif variableRef.datatype == 'DASHAMANSHA':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                    return 0

                expression = ex.makeExp(value)
                variableRef.value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                return 0

        elif variableRef.datatype == 'TARKA':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
                    return 0

                if value == 'SARI':
                    variableRef.value = True
                elif value == 'TAPPU':
                    variableRef.value = False
                else:
                    expression = ex.makeExp(value)
                    variableRef.value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
                return 0

    else:
        print(f"AstitvaDosha: {varName} hesurina astitva illa.")
        return 0

    return f"{varName} = {c._variables[varName].value}"