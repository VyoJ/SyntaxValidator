import ply.yacc as yacc

from lexer import tokens

err = 0

def p_switch(p):
    '''
    switch : ID LARROW SWITCH LPAREN expr COMMA cases RPAREN
    '''

def p_expr(p):
    '''
    expr    : NUM   
            | ID 
    '''

def p_cases(p):
    '''
    cases   : STRING COMMA cases
            | STRING EQUAL STRING COMMA cases 
            | STRING EQUAL STRING
            | STRING
    '''
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1], p[3]] + p[5]

def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()
while True:
    err = 0
    try:
        s = input('Enter the switch statement or enter 0 to leave: ')
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