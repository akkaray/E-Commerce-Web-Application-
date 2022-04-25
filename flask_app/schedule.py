from base import base
class schedule(base):
    def __init__(self):
        self.setup('RW_ScheduleTable')

    
 
## connected to  list - add in main.py(users)to verify, during add  email must contain @  and the password must be of 3 character
##  and add is connected to add.html   
    def verify_new(self):
        print('verify_new')
        
        if len(self.data[0]['EventEndTime']) < len(self.data[0]['EventStartTime']) :
            self.errors.append('Event End Time must be future date')
            
            
        print(self.data[0]['EventEndTime'])
            
        
            
        if len(self.errors)==0:
            return True
        else:
            return False
            
## connected to  list - update in main.py(users) to verify, during update email must contain @ 
##  and update is connected to edit.html          
    def verify_update(self):
        
        if len(self.data[0]['EventEndTime']) < len(self.data[0]['EventStartTime']) :
            self.errors.append('Event End Time must be future date')
            
        
        
        if len(self.errors)==0:
            return True
        else:
            return False
