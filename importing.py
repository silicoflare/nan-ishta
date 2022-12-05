def exe(value):
    tokens = value.split(' ')
    try:
        exec(f"import {tokens[0]}")
    except ModuleNotFoundError:
        print(f"AsthitvaDosha: {tokens[0]} hesarina module illa.\n")
