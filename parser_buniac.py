from rply import ParserGenerator
from ast_buniac import Number, Sum, Sub, Print,If,

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT','SCANF', 'OPEN_KEY','CLOSE_KEY', 'OPEN_PAR', 'CLOSE_PAR',
             'SEMI_COLON','DOTS','COMMA', 'SUM', 'SUB','MULT','DIV','OR','AND','NOT','BIGGER_THAN',
             'SMALLER_THAN','EQUAL_TO','DIFF','INT','CHAR','VOID','WHILE','IF','ELSE','FUNC']
        )
 #_____________PROGRAM___________________________________________ 
    def parse(self):
        @self.pg.production('program : statement')
        def program(p):
            return p[0]


 #_____________FUNCTION___________________________________________   
# funct
#     : 'f', variable , "(", variable, {",", variable} ,")" ,':'
#     |'{',statement ,'}'   
#     ;
    # @self.pg.production('statement : FUNC variable OPEN_PAREN variable OPEN_KEY COMMA variable CLOSE_KEY CLOSE_PAREN DOTS')
    # @self.pg.production('statement : OPEN_KEY statement CLOSE_KEY')

 #_____________STATEMENT___________________________________________  
#     statement
#    : 'if', paren_expr, '{',statement,'}' ,':'
#    | 'if', paren_expr ,'{',statement,'}' ,'else' ,'{',statement,'}' ,':'
#    | 'while', paren_expr, '{',statement,'}' ,':'
#    | 'print', paren_expr, ';'
#    | atribution
#    ;''

        @self.pg.production('statement : IF paren_expression OPEN_KEY statement CLOSE_KEY DOTS')
        def statement_if(p):
            return If( p[1], p[3])
        @self.pg.production('statement : IF paren_expression OPEN_KEY statement CLOSE_KEY ELSE  OPEN_KEY statement CLOSE_KEY DOTS')
        def statement_if_else(p):
            return IfElse( p[1], p[3], p[7])
        @self.pg.production('statement : WHILE paren_expression OPEN_KEY statement CLOSE_KEY DOTS')
        def statement_while(p):
            return IfElse( p[1], p[3])
        @self.pg.production('statement : PRINT paren_expression SEMI_COLON')
        def statement_print(p):
            return Print(p[1])
        # @self.pg.production('statement : attribution')
        # def atribution(p):
    
            

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
            return p[1]

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
                return Not(left)
            
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
            t_operator = p[1]
            if t_operator.gettokentype() == 'MULT':
                return Multiply(left, right)
            elif t_operator.gettokentype() == 'DIV':
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
            left = p[0]
            right = p[2]
            middle = p[1]
            if left.gettokentype() == 'SUM':
                return Plus(middle)
            elif left.gettokentype() == 'SUB':
                return Minus(middle) 
            elif left.gettokentype() == 'number':
                return left
            elif middle.gettokentype() == 'expression':
                return middle
            elif left.gettokentype() == 'variable':
                return left       
                
        
    #_____________ATTRIBUTION___________________________________________  
    # attribution
    #     : variable, '=', expression
    #     ;
        @self.pg.production('attribution : variable EQUAL_TO expression')
        def attribution(p):
            return
            
    #_____________VARIABLE___________________________________________  
    # variable
    #    : STRING, {STRING, INT, '_'}
    #    ;
        @self.pg.production('expression : STRING')
        @self.pg.production('expression : STRINGINT')
        @self.pg.production('expression : STRING_')
        @self.pg.production('expression : STRING_STRING')
        @self.pg.production('expression : STRING_INT')
        def variable(p):
            return String(p[0].value)
    #_____________NUMBER___________________________________________  
    # number
    #    : FLOAT
    #    ;
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
    #____________STRING__________________________________________  
    # STRING
    #    :  "A" | "B" | "C" | "D" | "E" | "F" | "G"
    #     | "H" | "I" | "J" | "K" | "L" | "M" | "N"
    #     | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
    #     | "V" | "W" | "X" | "Y" | "Z" 
    #     | "a" | "b"| "c" | "d" | "e" | "f" | "g" 
    #     | "h" | "i"| "j" | "k" | "l" | "m" | "n" 
    #     | "o" | "p"| "q" | "r" | "s" | "t" | "u" 
    #     | "v" | "w"| "x" | "y" | "z" ;
    #    ;
        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value)
    #_____________FLOAT___________________________________________  
    # FLOAT
    #    : INT, ['.', INT]
    #    ;
        @self.pg.production('expression : FLOAT')
        @self.pg.production('expression : INT.INT')
        def float(p):
            return Number(p[0].value)
    #_____________INTEGER___________________________________________  
    # INT
    #    : "0"|"1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    #    ;
        @self.pg.production('expression : INT')
        def integer(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()

        