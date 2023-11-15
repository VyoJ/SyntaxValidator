import ply.yacc as yacc
import ply.lex as lex

#Lex File:
tokens = ('ID', 'EQUALS', 'LARROW', 'NUMBER', 'STRING', 'RARROW')

err = 0

def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_LARROW = r'<-'
t_RARROW = R'->'
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc File:
def p_declaration(p):
    '''
    declaration : ID LARROW NUMBER
                | ID LARROW STRING
                | ID EQUALS NUMBER
                | ID EQUALS STRING
                | NUMBER RARROW ID
                | STRING RARROW ID
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