import ply.lex as lex

tokens = ('ID', 'LARROW', 'NUMBER', 'STRING', 'C', 'SEQ', 'LPAREN', 'RPAREN', 'COMMA', 'COLON', 'BY', 'EQUAL', 'LEN', 'BOOLEAN_MISSING')

def t_C(t):
    r'c'
    return t

def t_SEQ(t):
    r'seq'
    return t

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