#This can be a little flexible
# 3 Methods: takeTicket, parForParking, leaveGarage
# few attributes: tickets - list, parkingSpaces - list, currentTicket - dictionary


class Garage():

    def __init__(self):
        self.tickets = 10
        self.parkingSpaces = 5
        self.currentTicket = {}

    def TakeTicket(self):
        if self.parkingSpaces <= 0:
            print("Sorry, there is no parking space left.")
            return
        elif self.tickets > 0:
            self.tickets -= 1
        else:
            print("You have no tickets to give.")
            
        self.parkingSpaces -=1
        

       
    
    def payForParking(self, pay=None):
        
        pay = input("How much would you like to pay?: ")

        if int(pay) > 0:
            self.currentTicket['paid'] = True
            print("Thank you for paying! You have 15 minutes to exit the garage.")

        elif pay is None:
            print("We have not yet recieved payment.")

        elif int(pay) <= 0:
            print("We have not yet recieved payment.")

    

    def leaveGarage(self):
        if self.currentTicket.get('paid'):
            print("Thank you, have a nice day!")
            self.parkingSpaces += 1               
            self.tickets += 1 
            return

            
            
        else:
            pay = input("Please enter payment: ")
            
            while int(pay) <= 0:
                pay = input("Please enter a payment of 1 or more: ")
            else:
               print("Thank you, have a nice day!")
               self.parkingSpaces += 1               
               self.tickets += 1 
               return
               
            

    def run(self):
        if self.parkingSpaces <= 0:
            print("Sorry, there is no parking available.")
            return
        while True:
            x = input("Welcome to the parking garage! What do you want to do? GiveTicket/PayParking/Leave: ")
            if x.lower() == "leave":
                self.leaveGarage()
                break
            elif x.lower() == "giveticket":
                self.TakeTicket()
            elif x.lower() == "payparking":
                self.payForParking()
                break
            else:
                print("Invalid option, please type GiveTicket/PayParking/Leave (not case sensitive)")


garage = Garage()
garage.run()


