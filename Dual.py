class Dual:
    def __init__(self, value, derivative):
        self.value = value
        self.derivative = derivative

    def __add__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(self.value + other.value, self.derivative + other.derivative)

    def __sub__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(self.value - other.value, self.derivative - other.derivative)
    
    def __mul__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(self.value * other.value, self.value * other.derivative + self.derivative * other.value)

    def __pow__(self, other) -> 'Dual':
        return Dual(self.value ** other, other * self.value ** (other - 1) * self.derivative)

    def __truediv__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(self.value / other.value, (self.derivative * other.value - self.value * other.derivative) / other.value ** 2)
    
    def __radd__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(other.value + self.value, other.derivative + self.derivative)
    
    def __rsub__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(other.value - self.value, other.derivative - self.derivative)
    
    def __rmul__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(other.value * self.value, other.value * self.derivative + other.derivative * self.value)
    
    def __rtruediv__(self, other) -> 'Dual':
        if isinstance(other, (int, float)):
            other = Dual(other, 0)
        return Dual(other.value / self.value, (other.derivative * self.value - other.value * self.derivative) / self.value ** 2)
    
    def __neg__(self) -> 'Dual':
        return Dual(-self.value, -self.derivative)
    
    def __pos__(self) -> 'Dual':
        return Dual(self.value, self.derivative)
    
    def __repr__(self):
        return f'Dual({self.value}, {self.derivative})'

    def __str__(self):
        return f'{self.value} + {self.derivative}ε'

    def __eq__(self, other: 'Dual'):
        return self.value == other.value and self.derivative == other.derivative
