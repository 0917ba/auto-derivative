from abc import abstractmethod
from math import sin, cos, tan, exp, log
from Dual import *


class Function:
    @abstractmethod
    def __call__(self, x):
        pass

    @staticmethod
    def parameter():
        return IdentityFunction()
    
    def derivative(self, x):
        return self.__call__(Dual(x, 1)).derivative
    
    def __add__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(self, other, 'add')
        
    
    def __sub__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(self, other, 'sub')

    def __mul__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(self, other, 'mul')
    
    def __truediv__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(self, other, 'div')
    
    def __pow__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(self, other, 'pow')

    def __radd__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(other, self, 'add')
    
    def __rsub__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(other, self, 'sub')
    
    def __rmul__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(other, self, 'mul')
    
    def __rtruediv__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(other, self, 'div')
    
    def __rpow__(self, other) -> 'BinaryFunction':
        if not isinstance(other, Function):
            other = ConstantFunction(other)
        return BinaryFunction(other, self, 'pow')
    
    def __neg__(self) -> 'UnaryFunction':
        return UnaryFunction(self, 'neg')

    def __pos__(self) -> 'UnaryFunction':
        return UnaryFunction(self, 'pos')
    
    def __abs__(self) -> 'UnaryFunction':
        return UnaryFunction(self, 'abs')



class BinaryFunction(Function):
    def __init__(self, f: Function, g: Function, type: str):
        if not isinstance(f, Function) or not isinstance(g, Function):
            raise ValueError('f and g must be functions')
        
        if type not in ['add', 'sub', 'mul', 'div', 'pow']:
            raise ValueError('Invalid type')
        
        self.f = f
        self.g = g
        self.type = type
    
    def __evaluate(self, x, y):
        if self.type == 'add':
            return x + y
        elif self.type == 'sub':
            return x - y
        elif self.type == 'mul':
            return x * y
        elif self.type == 'div':
            return x / y
        elif self.type == 'pow':
            return x ** y
        else:
            raise ValueError('Invalid type')
        
    def __call__(self, x):
        return self.__evaluate(self.f(x), self.g(x))


class UnaryFunction(Function):
    def __init__(self, f: Function, type: str):
        if type == 'constant' or type == 'identity':
            pass

        elif not isinstance(f, Function):
            raise ValueError('f must be a function')
        
        elif type not in ['neg', 'pos', 'abs', 'pow', 'sin', 'cos', 'tan', 'exp', 'log', 'sqrt', 'identity', 'constant']:
            raise ValueError('Invalid type')
        
        self.f = f
        self.type = type

    def __evaluate(self, x):
        if self.type == 'neg':
            return -x
        elif self.type == 'pos':
            return x
        elif self.type == 'abs':
            return abs(x)
        elif self.type == 'pow':
            return x ** self.exponent
        elif self.type == 'sin':
            if isinstance(x, Dual):
                return Dual(sin(x.value), cos(x.value) * x.derivative)
            return sin(x)
        elif self.type == 'cos':
            if isinstance(x, Dual):
                return Dual(cos(x.value), -sin(x.value) * x.derivative)
            return cos(x)
        elif self.type == 'tan':
            if isinstance(x, Dual):
                return Dual(tan(x.value), x.derivative / cos(x.value) ** 2)
            return tan(x)
        elif self.type == 'exp':
            if isinstance(x, Dual):
                return Dual(exp(x.value), exp(x.value) * x.derivative)
            return exp(x)
        elif self.type == 'log':
            if isinstance(x, Dual):
                return Dual(log(x.value), x.derivative / x.value)
            return log(x)
        elif self.type == 'sqrt':
            return x ** 0.5
        else:
            raise ValueError('Invalid type')

    def __call__(self, x):
        return self.__evaluate(self.f(x))


class ConstantFunction(UnaryFunction):
    def __init__(self, value):
        super().__init__(None, 'constant')
        self.value = value
    
    def __call__(self, x):
        return self.value


class IdentityFunction(UnaryFunction):
    def __init__(self):
        super().__init__(None, 'identity')
    
    def __call__(self, x):
        return x


def Log(f):
    if not isinstance(f, Function):
        f = ConstantFunction(f)
    return UnaryFunction(f, 'log')


def Exp(f):
    if not isinstance(f, Function):
        f = ConstantFunction(f)
    return UnaryFunction(f, 'exp')


def Sin(f):
    if not isinstance(f, Function):
        f = ConstantFunction(f)
    return UnaryFunction(f, 'sin')


def Cos(f):
    if not isinstance(f, Function):
        f = ConstantFunction(f)
    return UnaryFunction(f, 'cos')

def Tan(f):
    if not isinstance(f, Function):
        f = ConstantFunction(f)
    return UnaryFunction(f, 'tan')