# -*- coding: utf-8 -*-

class SymbolTable():
    def __init__(self):
        self.ST = {} 
        self.ancestor = None

    def getValue(self, key):
        if key in self.ST:
            return self.ST.get(key)
        else:
            if self.ancestor:
                return self.ancestor.getValue(key)
            else:
                print(key)
                raise ValueError("Senpai")

    def createValue(self,key,value):
        self.ST['{}'.format(key)] = value


class Node():
    def __init__(self):
        self.value = None
        self.children = []
    def Evaluate():
        pass

class masterNode(Node):
    def __init__(self,children):
        self.children = children

    def Evaluate(self):
        ST = SymbolTable()
        for i in self.children:
            i.Evaluate(ST)

class returnNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,ST):
        ans = self.children[0].Evaluate(ST)
        return ans

class funcDec(Node):
    def __init__(self,value,children):
        self.value = value
        self.children = children
		
    def Evaluate(self,ST):
        ST.createValue(self.value,self)
        #symbolTable.setValue(self.value,self)

class funcCall(Node):
    def __init__(self,value,children):
        self.value = value
        self.children = children
        self.NewST = SymbolTable() #Passar a symboltable atual como ancestor

    def Evaluate(self,symbolTable):
        self.NewST.ancestor = ST
        func = ST.getValue(self.value)
        argsName = []
        for i in range(0, len(func.children)-1):
            if func.children[i] != None:
                for j in func.children[i].children:
                    argsName.append(j)
                #argsName.append(ref) #precisa guardar o nome da variável aqui
                func.children[i].Evaluate(self.NewST) #Declarou os argumentos na nova ST
                
        if len(self.children) != 0:
            for i in range(0,len(self.children)):
                self.NewST.createValue(argsName[i], self.children[i].Evaluate(ST)) #passar o valor dos filhos para a nova ST na ordem correta
        
        #Evaluate do ultimo filho (comandos)
        for e in func.children[len(func.children)-1].children:
            if isinstance(e,returnNode):
                return e.Evaluate(self.NewST)
            else:
                e.Evaluate(self.NewST)

class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,ST):
        return self.value

class VarDecNode(Node):
    def __init__(self,children):
        self.children = children

    def Evaluate(self,ST):
        for i in self.children:
            ST.createValue(i,None)

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, ST):
        if self.value == "=":
            ST.createValue(self.children[0],self.children[1].Evaluate(ST))
        else: 
            if self.value == '+':
                return self.children[0].Evaluate(ST)+self.children[1].Evaluate(ST)
            elif self.value == '-':
                return self.children[0].Evaluate(ST)-self.children[1].Evaluate(ST)
            elif self.value == '*':
                return self.children[0].Evaluate(ST)*self.children[1].Evaluate(ST)
            elif self.value == '/':
                return self.children[0].Evaluate(ST)//self.children[1].Evaluate(ST)
            elif self.value == '>':
                return self.children[0].Evaluate(ST)>self.children[1].Evaluate(ST)
            elif self.value == '<':
                return self.children[0].Evaluate(ST)<self.children[1].Evaluate(ST)
            elif self.value == '==':
                return self.children[0].Evaluate(ST)==self.children[1].Evaluate(ST)
            elif self.value == '&&':
                return self.children[0].Evaluate(ST) and self.children[1].Evaluate(ST)
            elif self.value == '||':
                return self.children[0].Evaluate(ST) or self.children[1].Evaluate(ST)

class PrintfNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,ST):
        print(self.children[0].Evaluate(ST))

class IfElseNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,ST):
        if self.children[0].Evaluate(ST):
            return self.children[1].Evaluate(ST)
        elif self.children[2] != None:
            return self.children[2].Evaluate(ST)

class WhileNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,ST):
        while self.children[0].Evaluate(ST):
            self.children[1].Evaluate(ST)

class StatmentsNode(Node):
    def __init__(self, children):
        self.children = children

    def Evaluate(self,ST):
        for i in self.children:
            i.Evaluate(ST)

class VarVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,ST):
        return ST.getValue(self.value)

