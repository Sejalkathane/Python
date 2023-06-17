# instance Variable:: eg: pin , balcnce : alwaya having diffrent value for diffrent object


class Car:
    
    def __init__(self):
        self.mil=10
        self.com="BMW"
    
print(Car)
c1=Car()
c2=Car()

c1.mil=8
c2.com=90
print(c1.com,c1.mil)
print(c2.com,c2.mil)

