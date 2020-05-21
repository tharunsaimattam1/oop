from math import sqrt

class ComplexNumber:
    
    def __init__(self, real_part=0, imaginary_part = 0):
        
        if (type(real_part) == str and type(imaginary_part) == str) or (type(real_part) == str and type(imaginary_part) == str):
            raise ValueError("Invalid value for real and imaginary part")
            
        if type(real_part) == int or type(real_part) == float:
            self._real_part = real_part
        else:
            raise ValueError("Invalid value for real part")
            
        if type(imaginary_part) == int or type(imaginary_part) == float:
            self._imaginary_part = imaginary_part
        else:
            raise ValueError("Invalid value for imaginary part")
        
            
    @property
    def real_part(self):
        return self._real_part
    
    @property
    def imaginary_part(self):
        return self._imaginary_part
        
        
    def conjugate(self):
        return ComplexNumber(self._real_part, -(self._imaginary_part))
            
    def  __str__(self):
        return f'{self._real_part}{self._imaginary_part:+}i'  
      
    def __add__(self, other):
        real_part = self._real_part + other._real_part
        imaginary_part = self._imaginary_part + other._imaginary_part
        return ComplexNumber(real_part, imaginary_part)
    
    def __sub__(self, other):
        real_part = self._real_part - other._real_part
        imaginary_part  = self._imaginary_part - other._imaginary_part
        return ComplexNumber(real_part, imaginary_part)
        
    def __mul__(self, other):
        real_part = (self._real_part * other.real_part) + (self._imaginary_part * other._imaginary_part * -1)
        imaginary_part = (self._real_part * other._imaginary_part) + (self._imaginary_part * other._real_part)
        return ComplexNumber(real_part, imaginary_part)
        
    def __truediv__(self, other):
        real_part = (self._real_part * other._real_part + self._imaginary_part * other._imaginary_part) / (other._real_part * other._real_part + other._imaginary_part * other._imaginary_part)
        imaginary_part = (self._imaginary_part * other._real_part - self._real_part *  other._imaginary_part) / (other._real_part * other._real_part + other._imaginary_part * other._imaginary_part)
        return ComplexNumber(real_part, imaginary_part)
      
    def __abs__(self):
        abs_value = sqrt(pow(self._real_part, 2) + pow(self._imaginary_part, 2))
        return round(abs_value, 3)

    def __eq__(self, other):
        return self._real_part == other._real_part and self._imaginary_part == other._imaginary_part