class grand:
    a='animal'
    def __init__(self,cow,dog):
        self.cow=cow
        self.dog=dog
    def display(self):
        print(self,cow)
class derived(Base):
    def __init__(self,cow,cowbaby):
        super().__init__(cow)