class Bank():
    def __init__(self,잔액,계좌주인,이자율):
        self.잔액=잔액
        self.계좌주인=계좌주인
        self.이자율=이자율
    def 정보(self):
        print("잔액:",self.잔액)
        print("계좌주인:",self.계좌주인)
        print("이자율:",self.이자율)
    def 현재잔액(self):
        print("잔액:",self.잔액)
    def 계좌주인이름(self):
        print("계좌주인:",self.계좌주인)
    def 이자율퍼센트(self):
        print("이자율:",self.이자율)
        
A=Bank(100000,"홍길동","1.5%")
print(A.정보())
print(A.현재잔액())
print(A.계좌주인이름())
print(A.이자율퍼센트())
