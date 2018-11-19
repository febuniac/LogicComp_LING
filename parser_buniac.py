from rply import ParserGenerator
from ast_buniac import Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT','SCANF', 'OPEN_KEY','CLOSE_KEY', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON','DOTS','COMMA', 'SUM', 'SUB','MULT','DIV','OR','AND','NOT','BIGGER_THAN',
             'SMALLER_THAN','EQUAL_TO','DIFF','INT','CHAR','VOID','WHILE','IF','ELSE']
        )
 #_____________PROGRAM___________________________________________ 
    def parse(self):
        @self.pg.production('program : statemenmt')
        def program(p):
            return statement


 #_____________FUNCTION___________________________________________   
funct
    : 'f', variable , "(", variable, {",", variable} ,")" ,':'
    |'{',statement ,'}'   
    ;
 #_____________STATEMENT___________________________________________  
#     statement
#    : 'if', paren_expr, '{',statement,'}' ,':'
#    | 'if', paren_expr ,'{',statement,'}' ,'else' ,'{',statement,'}' ,':'
#    | 'while', paren_expr, '{',statement,'}' ,':'
#    | 'print', paren_expr, ';'
#    | atribution
#    ;''
    @self.pg.production('statement : IF paren_expression OPEN_KEY statement CLOSE_KEY DOTS')
    @self.pg.production('statement : IF paren_expression OPEN_KEY statement CLOSE_KEY ELSE  OPEN_KEY statement CLOSE_KEY DOTS')
    @self.pg.production('statement : WHILE paren_expression OPEN_KEY statement CLOSE_KEY DOTS')
    @self.pg.production('statement : PRINT paren_expression SEMI_COLON')
    @self.pg.production('statement : attribution')
    def statement(p):
        left = p[0]
        right = p[2]
        operator = p[1]
        if operator.gettokentype() == 'SUM':
            return Sum(left, right)
        elif operator.gettokentype() == 'SUB':
            return Sub(left, right)
        elif operator.gettokentype() == None:
        return left
        

 #_____________PAREN_EXPRESSION__________________________________________  
# paren_expression
#     : '(', expression, ')'
#     | '(' ,bools, ')'
#     | '(' ,relats, ')'
#     ; 
    @self.pg.production('paren_expression : OPEN_PAR expression CLOSE_PAR')
    @self.pg.production('paren_expression : OPEN_PAR booleans CLOSE_PAR')
    @self.pg.production('paren_expression : OPEN_PAR relational_expression CLOSE_PAR')
    def paren_expression(p):
        

 #_____________BOOLEANS__________________________________________  
# bools
#     : expression, '//', expression
#     | expression, '&&', expression
#     | expression, '!',  expression
#     ;
    @self.pg.production('booleans : expression OR expression')
    @self.pg.production('booleans : expression AND expression')
    @self.pg.production('booleans : expression NOT expression')
    def booleans(p):
        left = p[0]
        right = p[2]
        bool_operator = p[1]
        if bool_operator.gettokentype() == 'OR':
            return Or(left, right)
        elif bool_operator.gettokentype() == 'AND':
            return And(left, right)
        elif bool_operator.gettokentype() == 'NOT':
            return Not(left, right)
        
 #_____________RELATIONAL_EXPRESSION___________________________________________  
# relats
#     : expression, '>',  expression
#     | expression, '<',  expression
#     | expression, '==', expression
#     | expression, '!=', expression
#     ;
    @self.pg.production('relational_expression : expression BIGGER_THAN expression')
    @self.pg.production('relational_expression : expression SMALLER_THAN expression')
    @self.pg.production('relational_expression : expression EQUAL_TO EQUAL_TO expression')
    @self.pg.production('relational_expression : expression DIFF expression')
    def relational_expression(p):
        left = p[0]
        right = p[2]
        relat_operator = p[1]
        if relat_operator.gettokentype() == 'BIGGER_THAN':
            return Bigger(left, right)
        elif relat_operator.gettokentype() == 'SMALLER_THAN':
            return Smaller(left, right)
        elif relat_operator.gettokentype() == 'EQUAL_TO':
            return Equal(left, right)
        elif relat_operator.gettokentype() == 'DIFF':
            return Different(left, right)
  
 #_____________EXPRESSION___________________________________________  
# expression
#    :term 
#    |term, '+', term
#    |term, '-', term
#    ;
        @self.pg.production('expression : term')
        @self.pg.production('expression : term SUM term')
        @self.pg.production('expression : term SUB term')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == None:
            return left

 #_____________TERM___________________________________________  
# term
#    : factor, '*', factor
#    | factor, '/', factor
#    ;
    @self.pg.production('term : factor MULT factor')
    @self.pg.production('term : factor DIV factor')
    def term(p):
        left = p[0]
        right = p[2]
        relat_operator = p[1]
        if relat_operator.gettokentype() == 'MULT':
            return Multiply(left, right)
        elif relat_operator.gettokentype() == 'DIV':
            return Divide(left, right)

 #_____________FACTOR___________________________________________  
# factor
#    : '+', factor
#    | '-', factor
#    | number
#    | '(',expression,')'
#    | variable
#    ;
    @self.pg.production('factor : SUM factor')
    @self.pg.production('factor : SUB factor')
    @self.pg.production('factor : number')
    @self.pg.production('factor : OPEN_PAR expression CLOSE_PAR')
    @self.pg.production('factor : variable')
    def factor(p):
    
 #_____________ATTRIBUTION___________________________________________  
# attribution
#     : variable, '=', expression
#     ;
    @self.pg.production('attribution : variable EQUAL_TO expression')
    def attribution(p):
 #_____________VARIABLE___________________________________________  
variable
   : STRING, {STRING, INT, '_'}
   ;
 #_____________NUMBER___________________________________________  
# number
#    : FLOAT
#    ;
  @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
 #____________STRING__________________________________________  
STRING
   :  "A" | "B" | "C" | "D" | "E" | "F" | "G"
    | "H" | "I" | "J" | "K" | "L" | "M" | "N"
    | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
    | "V" | "W" | "X" | "Y" | "Z" 
    | "a" | "b"| "c" | "d" | "e" | "f" | "g" 
    | "h" | "i"| "j" | "k" | "l" | "m" | "n" 
    | "o" | "p"| "q" | "r" | "s" | "t" | "u" 
    | "v" | "w"| "x" | "y" | "z" ;
   ;
 #_____________FLOAT___________________________________________  
FLOAT
   : INT, ['.', INT]
   ;
 #_____________INTEGER___________________________________________  
INT
   : "0"|"1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
   ;


    
        



        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()