import operator
from types import LambdaType
from slcl.exceptions import *
import slcl.symbol_table

symbols = slcl.symbol_table.SymbolTable()


class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return '<InstructionList {0}>'.format(self.children)

    def eval(self):
        """
        Evaluates all the class children and returns the result
        of their eval method in a list or returns an Break
        in case one is found
        """

        ret = []
        for n in self:
            if isinstance(n, Break):
                return n

            res = n.eval()

            if isinstance(res, Break):
                return res
            elif res is not None:
                ret.append(res)

        return ret


class BaseExpression:
    def eval(self):
        raise NotImplementedError()


class Break(BaseExpression):
    def __iter__(self):
        return []

    def eval(self):
        pass


class ReturnStatement(Break):
    def __init__(self, expr: BaseExpression):
        self.expr = expr

    def __repr__(self):
        return '<Return expr={0}>'.format(self.expr)

    def eval(self):
        return full_eval(self.expr)


def full_eval(expr: BaseExpression):
    """
    Fully evaluates the passex expression returning it's value
    """

    while isinstance(expr, BaseExpression):
        expr = expr.eval()

    return expr


class Primitive(BaseExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Primitive "{0}"({1})>'.format(self.value, self.value.__class__)

    def eval(self):
        return self.value


class Identifier(BaseExpression):
    is_function = False

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Identifier {0}>'.format(self.name)

    def assign(self, val):
        if self.is_function:
            symbols.set_func(self.name, val)
        else:
            symbols.set_sym(self.name, val)

    def eval(self):
        if self.is_function:
            return symbols.get_func(self.name)

        return symbols.get_sym(self.name)

class Assignment(BaseExpression):
    def __init__(self, identifier: Identifier, val):
        self.identifier = identifier
        self.val = val

    def __repr__(self):
        return '<Assignment sym={0}; val={1}>'.format(self.identifier, self.val)

    def eval(self):
        if self.identifier.is_function:
            self.identifier.assign(self.val)
        else:
            self.identifier.assign(self.val.eval())


class BinaryOperation(BaseExpression):
    __operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '**': operator.pow,
        '/': operator.truediv,
        '%': operator.mod,

        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,

        'and': lambda a, b: a.eval() and b.eval(),
        'or': lambda a, b: a.eval() or b.eval(),

        '&': operator.and_,
        '|': operator.or_,
        '^': operator.xor,
    }

    def __repr__(self):
        return '<BinaryOperation left ={0} right={1} operation="{2}">'.format(self.left, self.right, self.op)

    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        left = None
        right = None

        try:
            # find the operation that needs to be performed
            op = self.__operations[self.op]

            # The only lambda operations are logical and/or
            # Pass the arguments unevaluated as they will be during the lambda execution
            # This implements short circuit boolean evaluation
            if isinstance(op, LambdaType):
                return op(self.left, self.right)

            # otherwise, straight up call the operation, also save the variables
            # in case they are to be used for the exception block
            left = self.left.eval()
            right = self.right.eval()
            return op(left, right)
        except TypeError:
            fmt = (left.__class__.__name__, left, self.op, right.__class__.__name__, right)
            raise InterpreterRuntimeError("Unable to apply operation (%s: %s) %s (%s: %s)" % fmt)


class CompoundOperation(BaseExpression):
    __operations = {
        '+=': operator.iadd,
        '-=': operator.isub,
        '*=': operator.imul,

    }

    def __init__(self, identifier: Identifier, modifier: BaseExpression, operation: str):
        self.identifier = identifier
        self.modifier = modifier
        self.operation = operation

    def __repr__(self):
        fmt = '<Compound identifier={0} mod={1} operation={2}>'
        return fmt.format(self.identifier, self.modifier, self.operation)

    def eval(self):
        # Express the compound operation as a 'simplified' binary op
        # does not return anything as compound operations
        # are statements and not expressions

        l = self.identifier.eval()
        r = self.modifier.eval()

        try:
            self.identifier.assign(self.__operations[self.operation](l, r))
        except TypeError:
            fmt = (l.__class__.__name__, l, self.operation, r.__class__.__name__, r)
            raise InterpreterRuntimeError("Unable to apply operation (%s: %s) %s (%s: %s)" % fmt)


class UnaryOperation(BaseExpression):
    __operations = {
        '+': operator.pos,
        '-': operator.neg,
        '~': operator.inv,
        'not': operator.not_
    }

    def __repr__(self):
        return '<Unary operation: operation={0} expr={1}>'.format(self.operation, self.expr)

    def __init__(self, operation, expr: BaseExpression):
        self.operation = operation
        self.expr = expr

    def eval(self):
        return self.__operations[self.operation](self.expr.eval())


class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart

    def __repr__(self):
        return '<If condition={0} then={1} else={2}>'.format(self.condition, self.truepart, self.elsepart)

    def eval(self):
        if self.condition.eval():
            return self.truepart.eval()
        elif self.elsepart is not None:
            return self.elsepart.eval()


class For(BaseExpression):
    def __init__(self, variable: Identifier, start: Primitive, end: Primitive, asc: bool, body: InstructionList):
        self.variable = variable
        self.start = start
        self.end = end
        self.asc = asc  # ascending order
        self.body = body

    def __repr__(self):
        fmt = '<For start={0} direction={1} end={2} body={3}>'
        return fmt.format(self.start, 'asc' if self.asc else 'desc', self.end, self.body)

    def eval(self):
        if self.asc:
            lo = self.start.eval()
            hi = self.end.eval() + 1
            sign = 1
        else:
            lo = self.start.eval()
            hi = self.end.eval() - 1
            sign = -1

        for i in range(lo, hi, sign):
            self.variable.assign(i)

            # in case of break prematurely break the loop
            if isinstance(self.body.eval(), Break):
                break



class While(BaseExpression):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return '<While cond={0} body={1}>'.format(self.condition, self.body)

    def eval(self):
        while self.condition.eval():
            if isinstance(self.body.eval(), Break):
                break


class PrintStatement(BaseExpression):
    def __init__(self, items: InstructionList):
        self.items = items

    def __repr__(self):
        return '<Print {0}>'.format(self.items)

    def eval(self):
        print(*self.items.eval(), end='', sep='')


class FunctionCall(BaseExpression):
    def __init__(self, name: Identifier, params: InstructionList):
        self.name = name
        self.params = params

    def __repr__(self):
        return '<Function call name={0} params={1}>'.format(self.name, self.params)

    def __eval_builtin_func(self):
        func = self.name.eval()
        args = []

        for p in self.params:
            args.append(full_eval(p))

        return func.eval(args)

    def __eval_udf(self):
        func = self.name.eval()
        args = {}

        # check param count
        l1 = len(func.params)
        l2 = len(self.params)

        if l1 != l2:
            msg = "Invalid number of arguments for function {0}. Expected {1} got {2}"
            raise InvalidParamCount(msg.format(self.name.name, l1, l2))

        # pair the defined parameters in the function signature with
        # whatever is being passed on.
        #
        # On the parameters we only need the name rather than fully evaluating them
        for p, v in zip(func.params, self.params):
            args[p.name] = full_eval(v)

        return func.eval(args)

    def eval(self):
        if isinstance(self.name.eval(), BuiltInFunction):
            return self.__eval_builtin_func()

        return self.__eval_udf()


class Function(BaseExpression):
    def __init__(self, params: InstructionList, body: InstructionList):
        self.params = params
        self.body = body

    def __repr__(self):
        return '<Function params={0} body={1}>'.format(self.params, self.body)

    def eval(self, args):
        symbols.set_local(True)

        for k, v in args.items():
            symbols.set_sym(k, v)

        try:
            ret = self.body.eval()

            if isinstance(ret, ReturnStatement):
                return ret.eval()
        finally:
            symbols.set_local(False)

        return None


class BuiltInFunction(BaseExpression):
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        return '<Builtin function {0}>'.format(self.func)

    def eval(self, args):
        return self.func(*args)


