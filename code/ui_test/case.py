class test:
    def __init__(self, a):
        print(a)


A = test('a')
print(id(A))
B = test('b')
print(id(B))
