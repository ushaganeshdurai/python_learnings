class A:
    label = "A: Base class"

class B(A):
    label = "B: Biscuit"

class C(A):
    label = "C: Car"

class D(C,B):
    pass

obj = D()
print(obj.label)


