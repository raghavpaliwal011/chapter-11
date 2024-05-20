class person:
    country ="india"

    def takebreath(self):
        print("i am breathing ..... ")

class employee(person):
    company ="honda"

    def getsalary(self):
        print (f"salary is {self.salary}")

    def takebreath(self):
        print("i am an programmer , i am a living bieng so i am breathing")

class programmer(employee):
    company ="fiverr"

    def getsalary(self):
        print (f"no salary to programmer to programmer")

    def takebreath(self):
        print ("i am a programmer so i am breathing++...")


p = person()
p.takebreath()
#print(p.company) #throws an error
e = employee()
e.takebreath()
print (e.company)
pr = programmer()
pr.takebreath()
print (pr.company)
print (pr.country)