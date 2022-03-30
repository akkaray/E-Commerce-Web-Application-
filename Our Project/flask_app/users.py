from base import base
class users(base):
    def __init__(self):
        self.setup('AY_Users')
    def trylogin(self, username, passwd):
    
        sql = f"SELECT * FROM `{self.tn}` WHERE `email` = %s AND `pw`= %s;"
        self.cur.execute(sql,(username, passwd))
        self.data = []
        for row in self.cur:
            self.data.append(row)
        if len(self.data) == 0:
            return False
        else:
            return True