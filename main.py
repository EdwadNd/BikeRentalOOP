import BikeRental

def main():

    print("_____Welcome to Edwards Bike rental shop___________")
    shop = BikeRental.BikeRental(1000)

    while True:
        print("1. display available bikes")
        print("2. request a bike on hourly basis of $5") 
        print("3. request a bike on daily basis of $20") 
        print("4. request a bike on weekly basis of $60") 
        print("5. return a Bike")
        print("6 Exit\n\n")
        print("Enter choice: ")
        responce = input ()

        if responce == "1":
            print(shop.displayStock())
        elif responce ==  "2":
            print("how many bikes do u want? \n Enter Number :")
            n = input()
            shop.rentBikeOnHourlyBasis(n)
        elif responce == "3":
            print("how many bikes do u want? \n Enter Number :")
            n = input()
            shop.rentBikeOnDailyBasis(n)
        elif responce ==  "4":
            print("how many bikes do u want? \n Enter Number :")
            n = input()
            shop.rentBikeOnWeeklyBasis(n)
        elif responce == "6":
            break
        elif responce == "5":
            shop.returnBkike()
        else:
            print("wrong selection! TRY AGAIN")
    
    print("\n\n")


if  __name__ == "__main__":
    main()

