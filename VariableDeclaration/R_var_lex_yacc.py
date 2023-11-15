# Combined Lex and Yacc files so that they can refer to the same error variable to take care of some edge cases while testing syntax

import ply.yacc as yacc
import ply.lex as lex

# R Variable Declaration Syntax:
# varname <- value
# varname = value
# value -> varname

# Lex File:
tokens = ('ID', 'EQUALS', 'LARROW', 'NUMBER', 'STRING', 'RARROW', 'BOOLEAN_MISSING')

err = 0

# values can be numbers, strings, boolean values or NA
t_LARROW = r'<-'
t_RARROW = R'->'
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'

def t_BOOLEAN_MISSING(t):
    r'TRUE | FALSE | NA'
    return t

# Identifier naming rules in R:
# Consists of letters, digits, the period (‘.’) and the underscore.
# Must not start with a digit or an underscore, or with a period followed by a digit.
def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_ignore = ' \t\n'

# To handle lexing errors when illegal characters are detected
def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc File:

# Using BNF Grammar
# Grammar production rules defined by the function p_rulename(p) and are specified in the function's docstring
# Tokens (in capital) are analogous to Terminals and other rulenames can be used as Non-Terminals

def p_declaration(p):
    '''
    declaration : ID LARROW value
                | ID EQUALS value
                | value RARROW ID
    '''

def p_value(p):
    '''
    value   : STRING
            | NUMBER
            | BOOLEAN_MISSING
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

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")

