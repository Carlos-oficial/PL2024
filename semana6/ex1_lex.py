from ply import lex
import sys

tokens = (
    'NUMBER',
    'OP_PLUS',
    'OP_MINUS',
    'OP_TIMES',
    'OP_DIVIDE',
    'LPAR',
    'RPAR',
    'EQUALS',
    'VARIABLE',
    'CONSTANT',
    'STOP'
    )

t_NUMBER = r'\d+'
t_OP_PLUS = r'\+'
t_OP_MINUS = r'-'
t_OP_TIMES = r'\*'
t_OP_DIVIDE = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'
t_EQUALS = r'='
t_VARIABLE = r'[a-z]\w*'
t_CONSTANT = r'[A-Z]+'

def t_STOP(t):
    r'STOP'
    

t_ignore = " \n\t"

def t_newline(t):
    r'/n+'

lexer = lex.lex()
for line in sys.stdin:    
    lexer.input(line)
    while token := lexer.token():
        print(token)
    
    
    