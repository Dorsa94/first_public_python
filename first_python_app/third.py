class Student :
    def __init__(self , name, degree, passed):
        self.name = name
        self.degree = degree
        self.passed = passed
        
    
        
        
    def get_status(self):
        print(self.name + 'his degrees are ' + self.degree + 'his advarge degree is ' + "and his status is " + self.passed)


    def avrage_in(x):
        for i in x:
             g = (i.riazi + i.fizik + i.shimi)/ 3
        return g   


    # def passShodeYaNa(r):
    #     if(r) >= 12:
    #         student.passed = True
    #     else:
    #         student.passed = False
            
       
student1 = Student('ali' ,  17, False )
student2 = Student('mamad' , 15 , False )        



student1.get_status()