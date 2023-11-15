import ply.yacc as yacc

from lexer import tokens

err = 0

def p_declaration(p):
    '''
    declaration : ID LARROW FUNC LPAREN args RPAREN LBRACE statement RBRACE
    '''
    # p[0] = (p[5], p[8])

def p_args(p):
    '''
    args    :   empty 
            |   ID
            |   ID COMMA args
    '''

def p_statement(p):
    '''
    statement   :   ID statement
                |   ID
    '''

def p_empty(p):
    '''
    empty   :
    '''

def p_error(p):
    print("Syntax error")
    global err
    err = 1

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