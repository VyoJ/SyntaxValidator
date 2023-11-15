import ply.lex as lex
import ply.yacc as yacc

#Lex file
tokens = ('ID', 'LARROW', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'FUNC', 'COMMA', 'NUMBER', 'STRING')

err = 0

def t_FUNC(t):
    r'function'
    return t

def t_ID(t):
    r'[.]?[a-zA-Z_][a-zA-Z_.0-9]*'
    return t

t_LARROW = r'<-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'

t_ignore = ' \t'

def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    global err
    err = 1
    t.lexer.skip(1)

lexer = lex.lex()

#Yacc file
def p_declaration(p):
    '''
    declaration : ID LARROW FUNC LPAREN args RPAREN LBRACE statement RBRACE
    '''

def p_args(p):
    '''
    args    : empty 
            | argslist
    '''

def p_argslist(p):
    '''
    argslist    : ID
                | ID COMMA argslist
    '''

def p_statement(p):
    '''
    statement   : var_declare statement
                | var_declare
    '''

def p_var_declare(p):
    '''
    var_declare : ID LARROW STRING
                | ID LARROW NUMBER
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
        s = input('Enter the function declaration statement or enter 0 to leave: ')
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