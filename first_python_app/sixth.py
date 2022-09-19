class person:
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
    def show(self):
        print(f'this human has {self.age} years old !')
        
        
a = person('dorsa' , 28 , 'Female')
b = person('behnam' , 21 , 'male')

# print(a.__dict__)
 
b.show()