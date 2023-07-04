superscript = ['\b ', '', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def disintegrate(function:list):
    """
    미적분
    """
    resultFunction = []
    for i in range(len(function)):
        if i!=0:
            resultFunction.append( function[i]*i )
    
    return resultFunction

def integrate(function:list):
    """
    적분
    """
    resultFunction = ['c']
    for i in range(len(function)):
        resultFunction.append( function[i]/(i+1) )
    
    return resultFunction

def getValue(function, x, c=None):
    result = 0
    for i in range(len(function)):
        if function[i]=='c':
            if c==None:
                raise ValueError
            else:
                result += c
        else:
            result += (x**i) * function[i]
    
    return result

def printFunction(function:list):
    processedFunction = []

    for i in range(0, len(function)-1):
        if function[i]=='c' or function[i]>0:
            processedFunction.append( " + "+str(function[i]) )
        elif function[i]<0:
            processedFunction.append( " - "+str(-1*function[i]) )
        else:
            processedFunction.append( "" )
    processedFunction.append( str(function[-1]) )

    for i in range(len(processedFunction)-1, -1, -1):
        if processedFunction[i] != "":
            print(processedFunction[i] + 'x'+superscript[i], end='')
    
    print("\n")