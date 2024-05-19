from io import TextIOWrapper
import sys
from ply import  lex

reserved = {
    "select": "SELECT",
    "from": "FROM",
    "where": "WHERE",
}

tokens = [
   'ATTRIBUTE',
   'PLUS',
   'MINUS',
   'MULTIPLY',
   'DIVIDE',
   'MOREOREQUAL',
   'LESSOREQUAL',
   'MORE',
   'LESS',
   'NUMBER'
 ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MOREOREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_MORE = r'>'
t_LESS = r'<'


def t_ATTRIBUTE(t):
    r'\b[a-z|A-Z]+\b'
    t.type = reserved.get(t.value.lower(), "ATTRIBUTE")
    return t

def t_NUMBER(t):
    r'\d+[.]?\d*'
    if "." in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignored characters (spaces and tabs)
t_ignore  = ' \t,;'

# error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'" )
    t.lexer.skip(1)




def main(stdin: TextIOWrapper) -> None:
    lexer = lex.lex()
    
    for line in stdin:
        lexer.input(line)
        for token in lexer:
            if not token: break
            print(token)

if __name__ == "__main__":
    main(sys.stdin)