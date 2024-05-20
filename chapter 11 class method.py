## 


class employee:
    company = "camel"
    salary =10000
    location = "udaipur"

    # def changesalary(self,sal):
    #     self.__class__.salary = sal
    @classmethod
    def changesalary(cls,sal):
        cls.salary = sal

e = employee()
print (e.salary)
e.changesalary(455)
print (e.salary)
print (employee.salary)