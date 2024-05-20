class person:
    country = "india"

    def __init__(self):
        print("initializing person....\n")

    def takebreath(self):
        print("i am breathing ..... ")

class employee(person):
    company ="honda"

    def __init__(self):
        super().__init__()
        print("initializing employee....\n")

    def getsalary(self):
        print (f"salary is {self.salary}")

    def takebreath(self):
        super().takebreath()
        print("i am an programmer , i am a living bieng so i am breathing")

class programmer(employee):
    company ="fiverr"

    def __init__(self):
        #super().__init__()
        print("initializing programmer....\n")

    def getsalary(self):
        print (f"no salary to programmer to programmer")

    def takebreath(self):
        super().takebreath()
        print ("i am a programmer so i am breathing++...")


#p = person()
#p.takebreath()

#e = employee()
#e.takebreath()

pr = programmer()
#pr.takebreath()
