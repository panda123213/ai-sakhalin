import math

class Vector:
    def __init__(self,*coords):
        self.coords=list(coords)

    def __add__(self, other):
        if len(self.coords)!=len(other.coords):
            raise ValueError('размерность не совпадают')
        return Vector(*(a+b for a,b in zip(self.coords,other.coords)))

    def __mul__(self, scalar):
        return Vector(*(a*scalar for a in self.coords))

    def __repr__(self):
        return f'vector({self.coords})'

    def length(self):
        return math.sqrt(sum(a**2 for a in self.coords))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print("v1 + v2 =", v1 + v2)          # Vector([5, 7, 9])
print("v1 * 3 =", v1 * 3)            # Vector([3, 6, 9])
print("Длина v1 =", round(v1.length(), 2))  # 3.74