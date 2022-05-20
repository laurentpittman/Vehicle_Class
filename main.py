from vehicle import Vehicle
from electricVehicle import ElectricVehicle
from hybridVehicle import HybridVehicle
from battery import Battery

import datetime
import random

date = datetime.datetime.now()

class Main():
    print(date)
    print("Welcome to Cars.com! Buy and sell any cars. \n")

    answer = input("\nAre you a (1)customer or (2)employee? ")

    make = 0
    model = 0
    year = 0
    price = 0

    #initialize empty car object
    car = Vehicle(make,model,year,price)

    #add pre-existing car to database
    car1 = Vehicle("Hyundai", "Accent", 2020, 16000)
    car1.storeCar(car1)
    car2 = Vehicle("Toyota", "Camry", 2018, 18500)
    car2.storeCar(car2)
    car3 = Vehicle("Honda", "Accord", 2020, 25000)
    car3.storeCar(car3)

    #create a while loop for a employee
    user_input = True
    if(answer == "1"):
        while(user_input):
            print("\n  1. get car info\n  2. buy a car\n  3. sell a car\n  4. quit")
            answer = input("\nINPUT: ")

            #get car info
            if(answer == '1'):
                #finish -> print list
                car.showInfo()

            #buy a car
            elif(answer == '2'):
                car.buyCar()

            #sell a car
            elif(answer == '3'):
                car.sellCar()

            elif(answer == '4'):
                user_input = False #exit the program

            else:
                print("Invalid input: try again.")
    
    #create a while loop for a employee
    elif(answer == "2"):
        while(user_input):
            msg = "  1. create car\n  2. display cars\n  3. get car info\n  3. Type 'q' to exit\n"
            print(msg)
            answer = input("INPUT: ")

            #create a car and place in into the list
            if(answer == '1'):
                car.create()

            elif(answer == '2'):
                car.printList()

            elif(answer == '3'):
                 car.showInfo()    

            elif(answer == 'q'):
                user_input = False #exit the program

            else:
                print("Invalid input: try again.")


    
    
    
    
    
    
    
    
    
    
    '''car1 = Vehicle("Ford", "Mustang", 1964)

    car1.showInfo(car1)

    car1.updateMake(car1, "Dodge")
    car1.updateYear(car1, 1999)
    car1.updateMilage(car1, 54)

    car2 = Vehicle("Toyota", "Camry", 2018)
    car3 = Vehicle("Hyundai", "Accent", "2020")

    car4 = ElectricVehicle("Tesla", "Model 2", 2021)
    car5 = ElectricVehicle("Cheevy", "Bolt", 2019)

    car6 = HybridVehicle("Toyota", "Prius", 2007)
'''
    print("\n")
