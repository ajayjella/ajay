class student:
    def __init__(self,name,age,year,department):
        self.name=name
        self.age=age
        self.year=year
        self.department=department
    def work(self):
        if( self.department=='cse'):  
            print('software department')
        else:
            print('hardware department') 
a=student('pandu',22,3,'cse')
print(a.name)
print(a.age)
print(a.year)
print(a.department)
a.work()               