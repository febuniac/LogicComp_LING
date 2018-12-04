import ply.lex as lex
import slcl.exceptions

reserved = {
    'I': 'IF',
    'E': 'ELSE',
    'F': 'FOR',
    'W': 'WHILE',
    'B': 'BREAK',
    'f': 'FUNCTION',
    'R': 'RETURN',
    'P': 'PRINT',
    'A': 'AND',
    'O': 'OR',
    'N': 'NOT',
}

tokens = [
    'KEYWORD',
    'STRING',
    'NEWLINE',
    #_______SYMBOLS_____________
    'SEMICOLON',
    'COMMA',
    'COLON',
    #_______OPENERS & CLOSERS_____________
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_KEY',
    'CLOSE_KEY',
    #_______ARITHMETIC OPERATORS_____________
    'PLUS',
    'EXP',
    'MINUS',
    'MULT',
    'DIV',
    'MOD',
    'ASSIGN',
    #_______RELATIONAL OPERATORS_____________
    'EQUAL_TO',
    'DIFF',
    'GREATER_THAN',
    'GREATER_THAN_EQUAL',
    'LESS_THAN',
    'LESS_THAN_EQUAL',
    'VARIABLE',
    'NUM_INT',
    'NUM_FLOAT',
    'PLUS_EQ',
    'MINUS_EQ',
    'MULT_EQ',
    #_______BOOLEAN OPERATORS_____________
    'BIT_AND',
    'BIT_OR',
    'BIT_XOR',
    'BIT_NEG',
    'TRUE',
    'FALSE',


] + list(reserved.values())

t_ignore_WS = r'\s+'
t_ignore_COMMENTS = r'//.+'

#_______SYMBOLS_____________
t_COMMA = ','
t_COLON = ':'
t_SEMICOLON = ';'

#_______OPENERS & CLOSERS_____________
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_KEY = '{'
t_CLOSE_KEY = '}'

#_______ARITHMETIC OPERATORS_____________
t_PLUS = r'\+'
t_MINUS = '-'
t_MULT = r'\*'
t_DIV = r'/'
t_EXP = r'\*\*'
t_MOD = '%'
t_ASSIGN = '='

#_______RELATIONAL OPERATORS_____________
t_EQUAL_TO = '=='
t_DIFF = '!='
t_GREATER_THAN = '>'
t_GREATER_THAN_EQUAL = '>='
t_LESS_THAN = '<'
t_LESS_THAN_EQUAL = '<='
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_MULT_EQ = r'\*='

#_______BOOLEAN OPERATORS_____________
t_BIT_AND = r'\&'
t_BIT_OR = r'\|'
t_BIT_XOR = r'\^'
t_BIT_NEG = r'~'



def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.linepos = 0
    pass


def t_TRUE(t):
    'Tr'
    t.value = True
    return t


def t_FALSE(t):
    'Fa'
    t.value = False
    return t


def t_VARIABLE(t):
    r'[\$_a-zA-Z]\w*'

    t.type = reserved.get(t.value, t.type)

    return t


def t_NUM_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t


def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"(?:\\"|.)*?"'


    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")

    return t


def t_error(t):
    raise slcl.exceptions.UnexpectedCharacter("Unexpected character '%s' at line %d" % (t.value[0], t.lineno))


lexer = lex.lex()
