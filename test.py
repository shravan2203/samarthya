class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a + other.a
    def __str__(self):
        return str(self.a)
a=A(1)
b=A(2)
c=a+b
print(c)