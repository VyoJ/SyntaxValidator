import ply.lex as lex
import ply.yacc as yacc

# R function declaration Syntax:
# var <- c(value1, value2, value3, ...)
# var <- seq(value1, value2, by = value)
# var <- seq(value1, value2, length.out = value)
# var <- num1:num2
# Values in vector should be of same type but vectors consisting of number and strings can be implicity type converted and are correct syntax

# Lex file:

tokens = ('ID', 'LARROW', 'NUMBER', 'STRING', 'C', 'SEQ', 'LPAREN', 'RPAREN', 'COMMA', 'COLON', 'BY', 'EQUAL', 'LEN', 'BOOLEAN_MISSING')

err = 0

# To define the token for c function
def t_C(t):
    r'c'
    return t

# To define the token for seq function
def t_SEQ(t):
    r'seq'
    return t

# Arguments of the seq function
def t_BY(t):
    r'by'
    return t

def t_LEN(t):
    r'length.out'
    return t

def t_BOOLEAN_MISSING(t):
    r'TRUE | FALSE | NA'
    return t

def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_LARROW = r'<-'
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_COLON = r':'
t_EQUAL = r'='

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

# To handle syntax errors encountered while parsing
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

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")

