from base import base
import re                          # reg. expression
class transactions(base):
    def __init__(self):
        self.setup('AY_Transactions')
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
 
 
    def getopenTId(self,cid):
        sql = f'''SELECT * FROM AY_Transactions
                  where Tstatus=%s AND CID=%s'''
        self.cur.execute(sql,('open',cid))
        self.data = []
        for row in self.cur:
            self.data.append(row)
        if len(self.data)==0:#There is no open order for this cid
            d = {}
            d['Amount'] = 0
            d['Tdate'] = ''
            d['Tstatus'] = 'Open'
            d['Paymenttype'] = ''
            d['CID'] = cid
            self.add(d)
            self.insert()
            return self.data[0][self.pk]
        else:
            return self.data[0][self.pk]
            
            
            
    
  
        