from Car import Car

class EV(Car):
    __range = 0.0
    __gen = 0

    #constructors
    def __init__(self):
        super().__init__(0.0,"ELECTRIC CAR","BLACK (default)")
        self.__range = 100.0
        self.__gen = 1

    def __init__(self, speed: float=0.0, model: str="ELECTRIC CAR", color: str="BLACK (default)", range: float=100, gen: int=1):
        super().__init__(speed, model, color)
        self.__range = range
        self.__gen = gen
    
    #setters
    def setGen(self, gen: int):
        self.__gen = gen

    def setRange(self, range: float):
        self.__range = range

    #getters
    def getGen(self) -> int:
        return self.__gen

    def getRange(self) -> float:
        return self.__range

    def print(self):
        super().print()
        print("--this electric car has a range of: " + str(self.__range) + " milles per charge, generation: " + str(self.__gen) + ".")