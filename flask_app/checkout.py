from base import base
import re                          # reg. expression
class lineitems(base):
    def __init__(self):
        self.setup('AY_Line_items')
    
            
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
            
    def getprice(self):
        sql = f'''SELECT * FROM AY_Line_items
                  where TId=%s '''
        self.cur.execute(sql,(TId))
        self.data = []
        for row in self.cur:
            self.data.append(row)