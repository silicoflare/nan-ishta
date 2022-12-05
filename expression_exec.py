def makeExp(value):
    finalString = " "
    varName = ''

    value += ' '

    for i in range(len(value)):
        x = value[i]
        
        if (not x.isalpha() and x not in '_$'):
            if value[i-1].isalpha() or value[i-1] in '_$' and i!=0:
                if varName != '_temp_':
                    finalString += f"c._variables[\'{varName}\'].value"
                else:
                    finalString += f"c._temp_"
                varName = ''

        if not x.isalpha() and x not in '_$':
            finalString += x

        if x.isalpha() or x in '_$':
            varName += x

    return finalString.strip()