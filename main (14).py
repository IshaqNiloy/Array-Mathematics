import numpy

class Numpy():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print(a + b)
    
    def subtract(self):
        print(a - b)
    
    def multiply(self):
        print(a * b)

    def divison(self):
        print(a // b)

    def mod(self):
        print(a % b)

    def power(self):
        print(a ** b)

if __name__ == '__main__':
    row, column = map(int, input().split())
    #Using for loop to take multidimentional array as input
    a = numpy.array([input().split() for _ in range(row)], int)
    b = numpy.array([input().split() for _ in range(row)], int)
    my_object = Numpy(a, b)
    my_object.add()
    my_object.subtract()
    my_object.multiply()
    my_object.divison()
    my_object.mod()
    my_object.power()