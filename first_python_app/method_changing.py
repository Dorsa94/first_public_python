class javad():
    def __init__(self , data):
        self.data = data

    def mul_list(self , mul):
        self.old_data = self.data.copy()
        self.data = [x * mul for x in self.data]
        return self
        
    def merge(self):
        self.data = [ *self.old_data , *self.data]
        return self
         
    def show(self):
        print(self.data)
        
a = javad([1,5,9,16])
# methon chaining : 
a.mul_list(4).merge().mul_list(3).merge().show()
