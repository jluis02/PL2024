import ply.lex as lex

tokens = (
   'SELECT',
   'FROM',
   'WHERE',
   'DELIMITER1',
   'DELIMITER2',
   'ATTRIBUTE',
   'NUMBER',
   'OPERATOR'
)

t_SELECT    = r'(?i)select'
t_FROM   = r'(?i)from'
t_WHERE   = r'(?i)where'
t_DELIMITER1  = r','
t_DELIMITER2  = r';'
t_OPERATOR = r'(<|>|=)+'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

t_ATTRIBUTE  = r'\w+'

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'SELECT id, nome, salario FROM empregados WHERE salario>=820'

lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)