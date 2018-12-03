import ply.yacc as yacc
import slcl.ast as ast
from slcl.lexer import *
from slcl.exceptions import *

disable_warnings = False

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement : variable
              | expression
              | if_statement
    '''
    p[0] = p[1]

def p_break(p):
    '''
    statement : BREAK SEMICOLON
    '''
    p[0] = ast.Break()


def p_print_statement(p):
    '''
    statement : PRINT COLON OPEN_PAREN arguments CLOSE_PAREN SEMICOLON
    '''
    p[0] = ast.PrintStatement(p[4])


def p_compound_operations(p):
    '''
     statement : variable PLUS_EQ expression SEMICOLON
               | variable MINUS_EQ expression SEMICOLON
               | variable MULT_EQ expression SEMICOLON

    '''
    p[0] = ast.CompoundOperation(p[1], p[3], p[2])

def p_while_loop(p):
    '''
    statement : WHILE COLON expression OPEN_KEY statement_list CLOSE_KEY
    '''
    p[0] = ast.While(p[3], p[5])


def p_for_loop(p):
    '''
    statement : FOR COLON OPEN_KEY statement_list CLOSE_KEY
    '''
    p[0] = ast.While(ast.Primitive(True), p[4])


def p_function_declaration(p):
    '''
    statement : FUNCTION variable OPEN_PAREN arguments CLOSE_PAREN OPEN_KEY statement_list CLOSE_KEY
              | FUNCTION variable OPEN_KEY statement_list CLOSE_KEY
    '''
    p[2].is_function = True

    if len(p) == 9:
        p[0] = ast.Assignment(p[2], ast.Function(p[4], p[7]))
    else:
        p[0] = ast.Assignment(p[2], ast.Function(ast.InstructionList(), p[4]))


def p_return(p):
    '''
    statement : RETURN expression SEMICOLON
    '''
    p[0] = ast.ReturnStatement(p[2])


def p_function_call(p):
    '''
    expression : variable OPEN_PAREN arguments CLOSE_PAREN
    statement : variable OPEN_PAREN arguments CLOSE_PAREN SEMICOLON

    '''
    p[1].is_function = True
    p[0] = ast.FunctionCall(p[1], p[3])

def p_variable(p):
    '''
    variable : VARIABLE
    '''
    p[0] = ast.Identifier(p[1])


def p_arithmetics_op(p):
    '''
    expression : expression PLUS expression %prec PLUS
                | expression MINUS expression %prec MINUS
                | expression MULT expression %prec MULT
                | expression DIV expression %prec DIV
                | expression EXP expression %prec EXP
                | expression MOD expression %prec MOD
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

def p_booleans_op(p):
    '''
    expression : expression BIT_AND expression
            | expression BIT_OR expression
            | expression BIT_XOR expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])


def p_unary_operation(p):
    '''
    expression : PLUS expression %prec UPLUS
               | MINUS expression %prec UMINUS
               | BIT_NEG expression
               | NOT expression
    '''
    p[0] = ast.UnaryOperation(p[1], p[2])


def p_paren_expression(p):
    '''
    expression : OPEN_PAREN expression CLOSE_PAREN
    '''
    p[0] = p[2] if isinstance(p[2], ast.BaseExpression) else ast.Primitive(p[2])



def p_attribution(p):
    '''
    expression : variable ASSIGN assignable SEMICOLON
    '''
    p[0] = ast.Assignment(p[1], p[3])


def p_ifstatement(p):
    '''
    if_statement : IF COLON expression OPEN_KEY statement_list CLOSE_KEY 
    '''
    p[0] = ast.If(p[3], p[5])


def p_if_elsestatement(p):
    '''
    if_statement : IF COLON expression OPEN_KEY statement_list CLOSE_KEY ELSE COLON OPEN_KEY statement_list CLOSE_KEY 
    '''
    p[0] = ast.If(p[3], p[5], p[10])


def p_if_else_ifstatement(p):
    '''
    if_statement : IF COLON expression OPEN_KEY statement_list CLOSE_KEY ELSE COLON if_statement 
    '''
    p[0] = ast.If(p[3], p[5], p[9])



def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])
def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = ast.Primitive(p[1])

def p_relationals_operators(p):
    '''
    boolean : expression EQUAL_TO expression
            | expression DIFF expression
            | expression GREATER_THAN expression
            | expression GREATER_THAN_EQUAL expression
            | expression LESS_THAN expression
            | expression LESS_THAN_EQUAL expression
            | expression AND expression
            | expression OR expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]


def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              |
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    elif len(p) == 1:
        p[0] = ast.InstructionList()
    else:
        p[1].children.append(p[3])
        p[0] = p[1]


def p_expression(p):
    '''
    expression : primitive
               | STRING
               | variable
    '''
    p[0] = p[1]


def p_error(p):
    if p is not None:
        raise ParserSyntaxError("Syntax error at line %d, illegal token '%s' found" % (p.lineno, p.value))

    raise ParserSyntaxError("Unexpected end of input")


def get_parser():
    return yacc.yacc(errorlog=yacc.NullLogger()) if disable_warnings else yacc.yacc()