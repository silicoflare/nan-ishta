def makeExp(value):
    finalString = " "
    varName = ''

    value += ' '

    for i in range(len(value)):
        x = value[i]
        
        if (not x.isalpha()):
            if value[i-1].isalpha() and i!=0:
                finalString += f"c._variables[\'{varName}\'].value"
                varName = ''

        if not x.isalpha():
            finalString += x

        if x.isalpha():
            varName += x

    return finalString.strip()