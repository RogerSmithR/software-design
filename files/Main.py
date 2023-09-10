from Car import Car
from EV import EV

def main():
    # default constructors
    print("\n--CREATING CARS WITH DEFAULT CONSTRUCTORS\n")
    car = Car()
    car.print();
    electricCar = EV()
    electricCar.print()

    # parameterized constructors
    print("\n--CREATING CARS WITH PARAMETERIZED CONSTRUCTORS\n")
    pCar = Car(10,"FORD ESCAPE","RED")
    pCar.print()
    pEV = EV(15,"TESLA","WHITE",300,2)
    pEV.print();

    #setters and getters
    print("\n--CHANGING VALUES\n")
    pEV.setSpeed(20)
    pEV.setModel("FORD")
    pEV.setColor("RED METALLIC")
    pEV.setRange(200)
    pEV.setGen(3)
    print("Model: "+ pEV.getModel() + ", Color: "+pEV.getColor() + ", Speed: "+ str(pEV.getNumCars()) + ", Range: " + str(pEV.getRange()) + ", Generation: " + str(pEV.getGen()))

    #accelerating and decelerating
    print("\n--ACELERATING AND DECELERATING\n")
    print("--STARTING FROM 0 MPH. ROAD'S SPEED LIMIT: 20 MPH.\n")
    pEV.setSpeed(0)
    pEV.accelerate();
    print("--The driver accelerate the car. SPEED: " + str(pEV.getSpeed()) + " Mph.")
    pEV.accelerate();
    print("--The driver accelerate the car again. SPEED: " + str(pEV.getSpeed()) + " Mph.")
    pEV.accelerate();
    print("--The driver accelerate the car again. SPEED: " + str(pEV.getSpeed()) + " Mph.")
    print("The driver see the cops!!!")
    pEV.decelerate();
    print("--The driver decelerate the car. SPEED: " + str(pEV.getSpeed()) + " Mph.")
    pEV.decelerate();
    print("--The driver decelerate again the car. SPEED: " + str(pEV.getSpeed()) + " Mph.")
    print("TOO LATE!! TICKET FOR SPEEDING.")
    print("\n--FINISH. Cant of cars: " + str(pEV.getNumCars()) + "\n")
main()