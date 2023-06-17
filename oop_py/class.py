class Atm:
    # we can put  :: Attribute->variable
    # ither we put Behaviout -> Methods[function]

    #||||   SELF::   
            #  self call object
            # why self: class data only acess by only class object hear ie.self
    def __init__(self):
        # __""__ is kbow as magic method / special method
      
        #  in constructor we write those code which is not under user controll eg: data on when app start etc.....

        # init is a constructor:: It is run as soon as an object of a class is instantiated.
        # when that class object created then constructor run
        #  constructor name always __init__
        self.pin=""
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input(""" Hello , How Would you like to Proceed?
        1.Enter 1 to create pin 
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        elif user_input=="5":
            print("exit")



    def create_pin(self):
        self.pin=int(input("Enter your pin: "))
        print("Your Pin set successfully")


    def deposit(self):
        temp=int(input("Enter Your Pin: "))
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Your amount is Deposited successfullyj")
        else:
            print("Invalid Pin")


    def withdraw(self):
        temp=int(input("Enter Your Pin: "))
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")

     
    def check_balance(self):
        temp=int(input("Enter Your Pin: "))
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")







sbi=Atm()


print(sbi)


