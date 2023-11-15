import ply.lex as lex

tokens = ('ID', 'LARROW', 'LIST', 'NUM', 'STRING', 'C', 'LPAREN', 'RPAREN', 'COMMA', 'BOOLEAN_MISSING')

def t_C(t):
    r'c'
    return t

def t_BOOLEAN_MISSING(t):
    r'TRUE | FALSE | NA'
    return t

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

def t_error(t):
    print(f"Syntax Error: Illegal character found '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
data = input()
lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)