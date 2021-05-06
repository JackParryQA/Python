class Student:
    def __init__(self,name,age,s_class="student"):
        self.name=name
        self.age=age
        self.s_class=s_class

    def avg_test_score(self,test1,test2,test3):
        return (test1+test2+test3)/3


# Jack=Student("Jack", 23, "Computer Science")
Jack=Student("Jack", 23)

print(Jack.avg_test_score(70,60,65))
print(getattr(Jack, "s_class"))