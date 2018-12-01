from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Parenthesis
        self.lexer.add('OPEN_PAR', r'\(')
        self.lexer.add('CLOSE_PAR', r'\)')
        self.lexer.add('OPEN_KEY', r'\{')
        self.lexer.add('CLOSE_KEY', r'\}')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Comma
        self.lexer.add('COMMA', r'\,')
        # Quote
        self.lexer.add('QUOTE', r'\"')
        # Dots
        self.lexer.add('DOTS', r'\:')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'/')
        # Boolean Operators
        self.lexer.add('OR', r'\//')
        self.lexer.add('AND', r'\&&')
        self.lexer.add('NOT', r'\!')
        # Relational Operators
        self.lexer.add('BIGGER_THAN', r'\>')
        self.lexer.add('SMALLER_THAN', r'\<')
        self.lexer.add('EQUAL_TO', r'\==')
        self.lexer.add('DIFF', r'\!=')
        self.lexer.add('ASSIGN', r'=')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Types 
        self.lexer.add('INT', r'IN')
        self.lexer.add('CHAR', r'CH')
        self.lexer.add('VOID', r'VO')
        # While
        self.lexer.add('WHILE', r'W')
        # If - else
        self.lexer.add('IF', r'I')
        self.lexer.add('ELSE', r'E')
        # Print
        self.lexer.add('PRINT', r'P')
        # Scanf
        self.lexer.add('SCANF', r'S')
        # Function
        self.lexer.add('FUNC', r'F')
        # Main
        self.lexer.add('MAIN', r'M')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
        
        
        
        
        
        
        
        #Tipos de Token (constantes)




# EOF = "EOF" #end of file
        # # End Of String
        # self.lexer.add('EOF', r'eof')

# IDENTIFIER = "IDENTIFIER"
#  self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*')

# FUNCCALL="FUNCCALL"
