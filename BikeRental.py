import datetime

class BikeRental:
    
    def __init__(self, stock=0):

        self.stock = stock
    
    def displayStock(self):
        #print("we have currently {} rent.".format(self.stock))
        return f"we have currently {self.stock} bikes available  to rent."
    
    def rentBikeOnHourlyBasis(self,  n):
        no_of_hours = int(n)

        if no_of_hours <= 0:
            print("Number of bikes should be positive!")
            return None
        elif no_of_hours > self.stock:
            print("Sorry we currently have {} bikes availabele to rent." .format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("you have rented {} bike(s) on hourly basis today at {} hours ".format(no_of_hours, now.hour))
            print("you will be charged $5 for each hour per bike")
            print("we hope that you enjoy our service")
            
            self.stock -= no_of_hours
            return now
    
    def rentBikeOnDailyBasis(self, n):
        no_of_days = int(n)

        if no_of_days <= 0:
            print("Number of bikes should be positive!")
            return None
        elif no_of_days > self.stock:
            print("Sorry we currently have {} bikes availabele to rent." .format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("you have rented {} bike(s) on daily basis today at {} hours ".format(no_of_days, now.hour))
            print("you will be charged $20 for each day per bike")
            print("we hope that you enjoy our service")
            
            self.stock -= no_of_days
            return now
        
    def rentBikeOnWeeklyBasis(self,  n):
        no_of_weeks = int(n)
        
        if no_of_weeks <= 0:
            print("Number of bikes should be positive!")
            return None
        elif no_of_weeks > self.stock:
            print("Sorry we currently have {} bikes availabele to rent." .format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("you have rented {} bike(s) on weeklu basis today at {} hours ".format(no_of_weeks, now.hour))
            print("you will be charged $60 for each week per bike")
            print("we hope that you enjoy our service")
            
            self.stock -= no_of_weeks
            return now
    def returnBkike(self, request):
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0 

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now =datetime.datetime.now()
            rentalPeriod = now - rentalTime 

            if rentalBasis == 1:
                bill = round((rentalPeriod.seconds /3600)*5*numOfBikes)

            elif rentalBasis == 2:
                bill = round((rentalPeriod.days)*20*numOfBikes)
            
            elif rentalBasis == 2:
                bill = round((rentalPeriod.days/7)*60*numOfBikes)
            
            if(3 <= numOfBikes <= 5):
                print("you are  eligible for family package of 30 % discount off")
                bill = bill*0.7
            
            print("Thank you for returning Edwards bike(s). we hope you did not breakit!")
            print("that would be ${}".format(bill))

        else:
            print("are you sure you rented a bike with us?")
            return None