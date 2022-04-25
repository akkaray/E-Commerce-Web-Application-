from base import base
import re                          # reg. expression
class products(base):
    def __init__(self):
        self.setup('AY_Products')
    
            
    def verify_new(self):
        
            
            
            
        if len(self.errors)==0:
            return True
        else:
            return False
    def verify_update(self):
       
        
            
            
            
        if len(self.errors)==0:
            return True
        else:
            return False