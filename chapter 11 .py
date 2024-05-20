class employee:
    company ="google"

    def showDetails(self):
        print("this is an employee")

class programmer(employee):
    language = "Python"
    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this is an programmer")

e = employee()
e.showDetails()
p = programmer()
p.showDetails()
#print (p.company)