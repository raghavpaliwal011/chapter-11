class employee:
    company ="visa"
    ecode = 120
class freelaner:
    company = "fiver"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1
    
class programmer(employee,freelaner):
    name = "rohit"

p = programmer()
p.upgradelevel()
print (p.company)