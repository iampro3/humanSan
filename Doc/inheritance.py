# -*- coding : utf-8 -*-

class Employee:
    def __init__(self,name,tip = 3000):
        self.name = name
        self.tip = tip

    def sum_tip(self, amout):
        self.tip += amout
        return self.tip

# 상속화 : 부모 클래스의 메서드를 자식 클래스에서 사용 가능하도록 정의함
class Manager(Employee):

    def __init__(self, name, tip=50000, project =None):
        Employee.__init__(self, name, tip)
        self.project = project
        
    def display(self):
        print("Manager", self.name)

    def sum_tip(self, amout =0, bonus =2):
        if amout >0:
            # 부모 클래스의 sum_tip 으로 가서 self.tip를 계산하고 return self.tip를 실행하고 결과도 보여준다. 
            # manager외에도 요리사도 추가되고 실장되고 실장도 추가될 수 있기 때문에 부모 클래스에서 실행되도록 함
            Employee.sum_tip(self, amout * bonus)   
        else:
            Employee.sum_tip(self, amout)

if __name__ == "__main__":
     mng = Employee("Chloe")
     print(mng.name)    #chloe     
     mng.display("manager chloe")  # manager chloe
     print(mng.tip)
     mng.sum_tip(2000)
     print(mng.tip)


if __name__ == "__main__":
    mng = Manager("Evan")
    print(mng.name) # Evan
    mng.display() # Manager Evan
    print(mng.tip)
    mng.sum_tip(2000)
    print(mng.tip)
        
    
