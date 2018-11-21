#_________NUMBER________________________
class Number():
    def __init__(self, value):
        self.value = value
#_________STRING________________________
class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)
#_________BINOP________________________
class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right
#_________UNOP________________________
class UnOp():
    def __init__(self, left, right):
        self.left = left
#_________SUM________________________
class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

#_________MULT________________________
class Multiply(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
#_________DIV________________________
class Divide(BinaryOp):
    def eval(self):
        return self.left.eval() // self.right.eval()

#_________SUB________________________
class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

#_________OR________________________
class Or(BinaryOp):
    def eval(self):
        return self.left.eval() // self.right.eval()
#_________AND________________________
class And(BinaryOp):
    def eval(self):
        return ((self.left.eval()) & (self.right.eval()))
#_________NOT________________________
class Not(Unop):
    def eval(self):
        return !(self.left.eval())
#_________BIGGER________________________
class Bigger(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()
#_________SMALLER________________________
class Smaller(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval() 

#_________EQUAL________________________
class Equal(BinaryOp):
    def eval(self):
        return self.left.eval()  = self.right.eval()
#_________DIFF________________________
class Different(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()  
#_________PLUS________________________
class Plus(Unop):
    def eval(self):
        return +(self.left.eval())
#_________MINUS________________________
class Minus(Unop):
    def eval(self):
        return -(self.left.eval())   
#_________PRINT________________________
class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())