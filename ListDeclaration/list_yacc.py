import ply.yacc as yacc

from lexer import tokens
# from lexer import data

err = 0

def p_declaration(p):
    '''
    declaration : ID LARROW C LPAREN list RPAREN
                | ID LARROW NUMBER COLON NUMBER
    '''
    if len(p) != 6:
        p[0] = p[5]

def p_list(p):
    '''
    list    :   NUMBER 
            |   STRING
            |   NUMBER COMMA list
            |   STRING COMMA list
    '''

def p_error(p):
    print("Syntax error")
    global err
    err = 1
    raise SyntaxError

parser = yacc.yacc()
while True:
    err = 0
    try:
        s = input('Enter the variable declaration statement or enter 0 to leave: ')
    except EOFError:
        break
    
    if not s: 
        err = 0
        print("You entered nothing, try again!")
        continue
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)

    if err == 0:
        print("Valid syntax")
        # print(result)