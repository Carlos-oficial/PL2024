from ply import lex
import sys

tokens = (
    'NUMBER',
    'BOOLEAN',
    'WORD',
    'SQ_B_OPEN',
    'SQ_B_CLOSE',
    'COMMA'
    )

t_NUMBER = r'(([1-9]\d*)|0)(\.\d*)'
t_BOOLEAN = r''
t_WORD = r''
t_SQ_B_OPEN = r''
t_SQ_B_CLOSE = r''
t_COMMA = r''
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
    
    
    