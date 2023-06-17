# 1.Instance method 
# 2.class method 
# 3.Static method 



# if we work with instance veriable we use self
# if we use class veriable we use cls

class Student:
    school="sk"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # classmethod
    @classmethod 
    def info(cls):
        return cls.school

 
s1=Student(1,3,4)
s2=Student(9,8,5)


print(s1.avg())
print(s2.avg())

print(s1.info())
