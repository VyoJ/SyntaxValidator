import ply.lex as lex

tokens = ('ID', 'EQUALS', 'LARROW', 'NUMBER', 'STRING', 'RARROW')

def t_ID(t):
    r'\b([.]?[a-zA-Z_][a-zA-Z_.0-9]*)\b'
    return t

t_LARROW = r'<-'
t_RARROW = R'->'
t_EQUALS = r'='
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'

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