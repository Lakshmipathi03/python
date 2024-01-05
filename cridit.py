class Sbi:
    branch='palamaner'
    ifsc='sbi00026'
    manager='Jagan'
    loc='chittoor'

    def __init__(self,name,mob,acc,pan,bal):
        self.name = name
        self.mobile = mob
        self.account = acc
        self.pan = pan 
        self.balance = bal
    
    def credit(self,amt):
        self.balance+=amt

    def debit(self,amt):
        self.balance-=amt

    def update_mob(self,mob):
        self.mobile=mob

    @classmethod
    def change_mgr(cls,new):
        cls.manager = new

    @staticmethod
    def add(a,b):
        return a+b        

chandra=Sbi('nara chandra',9999898998,77091234,'CBNT0000W',1)
lokesh=Sbi('nara lokesh',8888889898,77091235,'CBNT0001T',1)
