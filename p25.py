class A:
    def __init__(self):
        print('Inside A')
        self.a = 'a'

class B:
    def __init__(self):
        print('Inside B')
        self.b = 'b'

class C(A,B):
    def __init__(self):
        print('Inside C')
        A.__init__(self)
        B.__init__(self)
        print(self.a,self.b)

C()
