class Dual:
    def __init__(self, value: float, derivative: float):
        self.value = value
        self.derivative = derivative

    def __add__(self, other: 'Dual') -> 'Dual':
        return Dual(self.value + other.value, self.derivative + other.derivative)

    def __mul__(self, other: 'Dual') -> 'Dual':
        return Dual(self.value * other.value, self.value * other.derivative + self.derivative * other.value)

    def __repr__(self):
        return f'Dual({self.value}, {self.derivative})'

    def __str__(self):
        return f'{self.value} + {self.derivative}ε'

    def __eq__(self, other: 'Dual'):
        return self.value == other.value and self.derivative == other.derivative

    def __sub__(self, other: 'Dual') -> 'Dual':
        return Dual(self.value - other.value, self.derivative - other.derivative)
