class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c = c
        
class derived(Base):

    def __init__(self,c,d,e):
        super().__init__(c)
        self.e = e
        self.d = d

obj = derived(6,56,58)

