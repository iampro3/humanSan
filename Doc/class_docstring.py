# -*- coding : utf-8 -*-
class Person:
    """
    사람을 표현하는 클래스
    '''
    Attributes
    -----------
    # 매개변수 선언
    name : str
        name of the person
    age : int
        age of the person
    
    Methods
    ---------
    info(extrainfo = ""):
        Print the person name, age and etv

    """

    def __init__(self, name, age):  # 생성자에 앞에 정의한 하라미터들을 입력한다.
        """
        Constructs all the necessary attributes for ths person object

        Parameters 
        ---------
            name : str
                name of the person
            age : int
                age of the person
        """
        self.name = name    # 외부에서 값이 입력 -> class 내부의 변수로 저정됨
        self.age = age

    # 클래스 Method (내장 메서드)
    def info(self, extrainfo=None):
        """
        Print the person's name, age, and etc

        If the parameter extrainfo is pass , then it is  appended to........

        Parameters 
        ---------
            extrainfo : str
                More info to be written(Default is None)

        Returns
        ---------
        None
        """

        print(f'내 이름은 {self.name}, 내 나이는 {self.age}임.' + str(extrainfo))
if __name__ == "__main__":
    human1 = Person("Chloe", age = 20)
    human1.info("나의 직장은 휴면")
    print(Person.__dir__)
    help(Person)

        
