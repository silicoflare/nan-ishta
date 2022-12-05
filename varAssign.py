import _core as c
import expression_exec as ex

def exe(varName, value):
    # print(f"{varName} = {value}")
    if varName in c._variables:
        if c._variables[varName].datatype == 'SANKHYE':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                    return 0

                expression = ex.makeExp(value)
                c._variables[varName].value = int(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" SANKHYE moulya alla.")
                return 0
            except KeyError as ke:
                print(f"AstitvaDosha: {ke} hesurina astitva illa.")
                return 0
        
        elif c._variables[varName].datatype == 'DASHAMANSHA':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                    return 0

                expression = ex.makeExp(value)
                c._variables[varName].value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" DASHAMANSHA moulya alla.")
                return 0
            except KeyError as ke:
                print(f"AstitvaDosha: {ke} hesurina astitva illa.")
                return 0

        elif c._variables[varName].datatype == 'TARKA':
            try:
                if value[0] == '"' or value[0] == "'":
                    print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
                    return 0

                if value == 'SARI':
                    c._variables[varName].value = True
                elif value == 'TAPPU':
                    c._variables[varName].value = False
                else:
                    expression = ex.makeExp(value)
                    c._variables[varName].value = float(eval(expression))
            except ValueError:
                print(f"MoulyaDosha: \"{value}\" TARKA moulya alla.")
                return 0
            except KeyError as ke:
                print(f"AstitvaDosha: {ke} hesurina astitva illa.")
                return 0
        
        elif c._variables[varName].datatype == 'SHABDA':
            try:
                expression = ex.makeExp(value)
                # print(f"Damn: {expression}")
                c._variables[varName].value = eval(expression)
            except KeyError as ke:
                print(f"AstitvaDosha: {ke} hesurina astitva illa.")
                return 0

    else:
        print(f"AstitvaDosha: {varName} hesurina astitva illa.")
        return 0

    # print(f"{varName} = {c._variables[varName].value}")
    return f"{varName} = {c._variables[varName].value}"