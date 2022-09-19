class A:
    def __init__(self ,  name = None , age = None):
        self.name =name
        self.age = age
        
    def __bool__(self):
        return bool(self.name)
        
a1 = A('Dorsa' , age=None)

# if a1:
#     print('ok')
    
    
    
class MyList:
    def __init__(self , tedad=1):
        self.my_list = [None] * tedad
        
        
    def __repr__(self):
        return str(list(self.my_list))
    
    
    # __setitem__
    def self_item(self , index,value) :
        self.my_list[index] = value
    
    # __getitem__
    def get_item(self , index) :
        return  self.my_list[index] 
    
    # __delitem__
    def del_item(self , index) :
       del self.my_list[index] 
    
a = MyList(4)
# a.self_item(3,'Dorsa khar ast')
# print(a.get_item(3))
a.del_item(3)
print(a)   