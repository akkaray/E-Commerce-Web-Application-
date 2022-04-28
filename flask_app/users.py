from base import base
class users(base):
    def __init__(self):
        self.setup('AY_Users')

    def trylogin(self, username, passwd):
        print(username,passwd)
        sql = f"SELECT * FROM `{self.tn}` WHERE `email` = %s AND `pw`= %s;"
        self.cur.execute(sql,(username, passwd))
        self.data = []
        for row in self.cur:
            self.data.append(row)
        if len(self.data) == 0:
            return False
        else:
            return True
    def verify_new(self):
        print('verify_new')
        if '@' not in self.data[0]['email']:
            self.errors.append('Email address must contain @')
        if len(self.data[0]['pw'])<3:
            self.errors.append('Password must be more than 3 characters')
            
            
            
        if len(self.errors)==0:
            return True
        else:
            return False
    def verify_update(self):
       
        if '@' not in self.data[0]['email']:
            self.errors.append('Email address must contain @')
        
            
            
            
        if len(self.errors)==0:
            return True
        else:
            return False
