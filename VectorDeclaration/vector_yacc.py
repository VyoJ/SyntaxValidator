import ply.yacc as yacc

from lexer import tokens

err = 0

def p_declaration(p):
    '''
    declaration : ID LARROW C LPAREN list RPAREN
                | ID LARROW NUMBER COLON NUMBER
                | ID LARROW SEQ LPAREN NUMBER COMMA NUMBER COMMA BY EQUAL NUMBER RPAREN
                | ID LARROW SEQ LPAREN NUMBER COMMA NUMBER COMMA LEN EQUAL NUMBER RPAREN
    '''
    if len(p) != 6:
        p[0] = p[5]

def p_list(p):
    '''
    list    :   NUMBER 
            |   STRING
            |   BOOLEAN_MISSING
            |   NUMBER COMMA list
            |   STRING COMMA list
            |   BOOLEAN_MISSING COMMA list
    '''

def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()
while True:
    err = 0
    try:
        s = input('Enter the vector declaration statement or enter 0 to leave: ')
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