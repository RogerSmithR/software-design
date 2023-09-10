from Vehicle import Vehicle

class Car(Vehicle):
    __speed = 0.0
    __model = ""
    __color = ""
    numCars = 0

    #constructors
    def __init__(self):
        self.__speed = 0.0
        self.__model = "CAR"
        self.__color = "RED (default)"
        Car.numCars += 1

    def __init__(self, speed: float=0.0, model: str="CAR", color: str="RED (default)"):
        self.__speed = speed
        self.__model = model
        self.__color = color
        Car.numCars += 1
    
    #aceleration functions
    def accelerate(self) -> float:
        self.__speed += 10
        return self.__speed

    def decelerate(self) -> float:
        self.__speed -= 10
        return self.__speed

    #setters
    def setSpeed(self, speed: float):
        self.__speed = speed

    def setModel(self, model: str):
        self.__model = model

    def setColor(self, color: str):
        self.__color = color

    #getters
    def getSpeed(self) -> float:
        return self.__speed

    def getModel(self) -> str:
        return self.__model
    
    def getColor(self) -> str:
        return self.__color

    def getNumCars(self) -> int:
        return self.numCars

    #other functions
    def print(self):
        print("Model: " + self.__model + ", speed: " + str(self.__speed) + " mph, color: " + self.__color + ".")