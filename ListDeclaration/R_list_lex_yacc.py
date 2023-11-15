import ply.yacc as yacc
import ply.lex as lex

# R list declaration Syntax:
# var <- list( value1, value2, ..., vec, ..., list, ... )  
# Values in list can be of any type including list, vector, matrix, etc. 
# Implemented only list containing numbers, strings, booleans, vectors and lists.

# Lex file:
tokens = ('ID', 'LARROW', 'LIST', 'NUM', 'STRING', 'C', 'LPAREN', 'RPAREN', 'COMMA', 'BOOLEAN_MISSING')

err = 0

# To define the token for c function
def t_C(t):
    r'c'
    return t

def t_BOOLEAN_MISSING(t):
    r'TRUE | FALSE | NA'
    return t

# To define the token for list function
def t_LIST(t):
    r'list'
    return t

def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_LARROW = r'<-'
t_NUM = r'\d+'
t_STRING = r'"[^"]*"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

t_ignore = ' \t\n'

# To handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc File:

def p_declaration(p):
    '''
    declaration : ID LARROW LIST LPAREN values RPAREN
    '''

def p_values(p):
    '''
    values  : types COMMA values
            | types
    '''

def p_types(p):
    '''
    types   : ID
            | C LPAREN values RPAREN
            | STRING
            | NUM
            | BOOLEAN_MISSING
            | LIST LPAREN values RPAREN
    '''

# To handle syntax errors encountered while parsing
def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()
while True:
    err = 0
    try:
        s = input('Enter the list declaration statement or enter 0 to leave: ')
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

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")

