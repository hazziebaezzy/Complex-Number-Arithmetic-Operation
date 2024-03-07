import math

class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        
        self.real = float(real)
        self.imaginary = float(imaginary)
        
    def getRealPart(self):
        return self.real
    
    def getImaginaryPart(self):
        return self.imaginary
    
    def abs(self):
        return math.sqrt(self.real**2 + self.imaginary ** 2)
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
        
    def __add__(self, other):
        return Complex(self.real + other.getRealPart(), self.imaginary + other.getImaginaryPart())
        
    def __sub__(self, other):
        return Complex(self.real - other.getRealPart(), self.imaginary - other.getImaginaryPart())
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imag_part)
        
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("Division by zero")
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real_part, imag_part)
        
    
    