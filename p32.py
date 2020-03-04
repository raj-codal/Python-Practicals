class B:
    def __init__(self):
        print('Inside B')
        self.b = 'b'

class C(B):
    def __init__(self):
        print('Inside C')
        super().__init__()
        print(self.b)

C()
