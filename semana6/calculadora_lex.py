import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAR',
    'RPAR'
    )

t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'

t_ignore = " \n\t"

def t_newline(t):
    r'/n+'

lexer = lex.lex()
lexer.input("4 * (2 + 3) \n 1")
while token := lexer.token():
    print(token)
    
    
    