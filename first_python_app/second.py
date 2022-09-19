import os,glob
from khayyam import JalaliDatetime



# /home/dorsa/./Downloads
folder = input('insert your address : ')
format_set = set()
dt = JalaliDatetime.now().strftime('%A %d %B %Y')



files = glob.glob(folder + '/*')
# print (files)

for i in files:
   format = i.split('.').pop()
   format_set.add(format)
   
   
   
def mk_dr():
    for f in format_set:
        try:
            os.makedirs(folder + dt + '/' + f) 
        except:
            continue
        
def move_files():
    
    for file in files:
        try:
            
            format1 = file.split('.').pop()
        
            to_this = folder + '/' + format1 + "/" + file.split('/').pop()
            
            # print(to_this)
            
            # rename addresse un file ro taghir mide
            os.rename(file, to_this)
            
        except:
            continue



    
    
    
    
mk_dr()
move_files()
# print(format_set)