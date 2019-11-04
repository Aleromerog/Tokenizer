from read_file import readFile

logic_operators = ['==', '>' , '>=', '<', '<=', '!=']
unary_operators = ['=', '+', '+=', '-', '-=']
OP = ['(', ')', ':', ',', '[', ']']
reserved_words = ['and', 'except', 'lambda', 'with', 'as', 'finally', 'nonlocal', 'while',
                  'assert', 'false', 'None','yield','break', 'for','not','class','from', 'or',
                  'continue','global','pass','def','if','raise','del', 'import', 'return','elif',
                  'in','True','else','is','try']

def main():
    #Lista de los tokens
    tokenList = []
    #Nombre del archivo
    file = readFile('demo.py')
    #Variable para ir concatenando la cadena leída
    expretion = ''
    #Variable para concatenar un operador
    operators = ''
    #Variable para identificar si es un string lo que se esta leyendo
    isString = False
    for c in file:
        #Completar el operador y en caso de que sea de longitud mas de uno juntarlo
        if operators != '':
            if c in logic_operators or c in unary_operators:
                operators += c
            n = ['OPERATOR' , operators]
            tokenList.append(n)
            operators = ''
        else:
            operators = ''
        #En caso de que encuentre una apertura de cadena " ' ' " 
        if c == "\'": 
            if not isString:
                isString = True
                expretion += c
            else:
                expretion += c
                tokenList.append(['STRING', expretion])
                isString = False
                expretion = ''

        #Parar si hay un espacio o un operador
        elif (c == ' ' or c in logic_operators or c in unary_operators or c in OP) and not isString:
            #Identifica y concatena unicamente si es un operador
            if c in logic_operators or c in unary_operators:
                operators += c
            #Identifica si la cadena es palabra reservada y la agrega a la lista de tokens
            if expretion in reserved_words:
                n = ['RESERVED' , expretion]
                tokenList.append(n)
            #Identifica si la cadena es un numero y la agrega a la lista de tokens
            elif expretion.isdigit():
                n = ['CONSTANT' , expretion]
                tokenList.append(n)
            #Identifica si la cadena es una palabra y la agrega a la lista de tokens
            elif expretion != '':
                n = ['NAME' , expretion]
                tokenList.append(n)
            if c in OP:
                n = ['OP', c]
                tokenList.append(n)
            expretion = ''

        else:
            expretion += c
        
    

    printList(tokenList)

def printList(tokenList):
    for token in tokenList:
        print(token)

if __name__== "__main__":
      main()
