class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s1=student("a",20)
s1.display()   
s2=student("b",25)
s2.display()     
