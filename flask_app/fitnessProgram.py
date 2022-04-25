from base import base
class fitnessProgram(base):
    def __init__(self):
        self.setup('RW_FitnessProgram')

    
 
## connected to  list - add in main.py(users)to verify, during add  email must contain @  and the password must be of 3 character
##  and add is connected to add.html   
    def verify_new(self):
        print('verify_new')
        
        if len(self.data[0]['ProgramName']) < 2:
            self.errors.append('ProgramName must be more than 3 characters')
            
        
            
        if len(self.errors)==0:
            return True
        else:
            return False
            
## connected to  list - update in main.py(users) to verify, during update email must contain @ 
##  and update is connected to edit.html          
    def verify_update(self):
        
        if len(self.data[0]['ProgramName']) < 2:
            self.errors.append('ProgramName must be more than 3 characters')
            
        
        
        if len(self.errors)==0:
            return True
        else:
            return False
