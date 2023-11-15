import ply.lex as lex
import ply.yacc as yacc

# R switch statement Syntax:
# var <- switch (expression, case 1, case 2, ...)
# var = switch (expression, case 1, case 2, ...)
# switch (expression, case 1, case 2, ...)

# Lex file:
tokens = ('ID', 'LARROW', 'LPAREN', 'RPAREN', 'COMMA', 'STRING', 'NUM', 'EQUAL', 'SWITCH')

err = 0

# To detect switch keyword as a token
def t_SWITCH(t):
    r'switch'
    return t

def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_LARROW = r'<-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_EQUAL = r'='
t_NUM = r'\d+'
t_STRING = r'"[^"]*"'

t_ignore = ' \t'

# To handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc File:

def p_switch(p):
    '''
    switch  : ID LARROW SWITCH LPAREN expr COMMA cases RPAREN
            | ID EQUAL SWITCH LPAREN expr COMMA cases RPAREN
            | SWITCH LPAREN expr COMMA cases RPAREN
    '''

def p_cases(p):
    '''
    cases   : STRING COMMA cases
            | casevalue EQUAL STRING COMMA cases 
            | casevalue EQUAL STRING
            | STRING
    '''

# To derive either an identifier or string value
def p_casevalue(p):
    '''
    casevalue   : STRING
                | ID
    '''

# Expression can be numeric or an identifier value
def p_expr(p):
    '''
    expr    : NUM   
            | ID
            
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

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")

