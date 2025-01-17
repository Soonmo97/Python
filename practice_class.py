class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
        # 다중 상속시에는 super()는 맨 처음 클래스의 생성자 하나만 호출되므로
        # Unit.__init__과 같은 방식으로 따로 모두 호출해야함

# 드랍쉽
dropship = FlyableUnit()