from base import base
import re                          # reg. expression
class addresses(base):
    def __init__(self):
        self.setup('demo_addresses')
    def verify_new(self):
        self.data[0]['zip']=re.sub('[^0-9]+', '', self.data[0]['zip'])    # reg. expression (change others to number)
        if len(self.data[0]['zip'])!=5:
            self.errors.append('Zipcode must be 5 digits')
        
        if len(self.errors)==0:
            return True
        else:
            return False
            
            
    def verify_update(self):
        self.data[0]['zip']=re.sub('[^0-9]+', '', self.data[0]['zip'])
        if len(self.data[0]['zip'])!=5:
            self.errors.append('Zipcode must be 5 digits')
           
        if len(self.errors)==0:
            return True
        else:
            return False
 
 
    def getAllwithusers(self):
       
        sql = f'''SELECT * FROM demo_addresses
                  LEFT JOIN demo_users ON demo_users.id = demo_addresses.uid'''
        self.cur.execute(sql)
        self.data = []
        for row in self.cur:
            self.data.append(row)