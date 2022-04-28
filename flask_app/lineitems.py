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
            
    def getTId(self,TId):
        sql = f'''SELECT * FROM AY_Line_items 
        left join AY_Products on AY_Products.ProductId=AY_Line_items.ProductId where TId=%s  '''
                  
        self.cur.execute(sql,(TId))
        self.data = []
        for row in self.cur:
            self.data.append(row)
    def getTotal(self):
        total=0
        for item in self.data:
            total+=item['PPrice']*item['Quantity']
        return total
        