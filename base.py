import pymysql, mysecrets

class base():
    def setup(self, table):

        self.data = []
        self.tn = table
        self.fields = []
        self.conn = None
        self.cur = None
        self.pk = None
        self.getFields()
    def connect(self):

        self.conn = pymysql.connect(host = mysecrets.host, port = 3306, user = mysecrets.user,
                       passwd = mysecrets.passwd, db = 'is437', autocommit = True)

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def close(self):

        self.cur.close()
        self.conn.close()

    def getFields(self):

        self.connect()
        sql = f'''DESCRIBE `{self.tn}`;'''
        self.cur.execute(sql)
        for row in self.cur:
            if 'auto_increment' in row['Extra']:
                self.pk = row['Field']
            else:
                self.fields.append(row['Field'])

    def add(self, d):
        self.data.append(d)

    def insert(self,n=0):
        sql = f'INSERT INTO {self.tn} ('
        #{fields[0]}, {fields[1]}, {fields[2]}, {fields[3]});'
        vals = ''
        value_list = []
        for field in self.fields:
            sql += f'`{field}`,'+' '
            vals += '%s, '
            value_list.append(self.data[n][field])
        sql = sql[0:-2]
        vals = vals[0:-2]
        #INSERT INTO users (uid,username,fname,lname) VALUES (%s, %s, %s, %s);
        sql += ') VALUES '
        sql += f'({vals});'
        #print(sql,value_list)
        self.cur.execute(sql, value_list)
    def getAll(self):
        sql = f"SELECT * FROM `{self.tn}` "
        self.cur.execute(sql)
        self.data = []
        for row in self.cur:
            self.data.append(row)
    def getById(self,id):
        sql = f"SELECT * FROM `{self.tn}` WHERE `{self.pk}` = %s;"
        self.cur.execute(sql,id)
        self.data = []
        for row in self.cur:
            self.data.append(row)
    def update(self,n=0):
        #UPDATE table SET field= %s .... WHERE pk = %s
        fl = []
        for fn in self.fields:
            if fn in self.data[n].keys():#dont try to update the field if the data doesnt exist
                fl.append(fn)
        fvs= '`'+'`=%s, `'.join(fl) + '`=%s'
        idval = self.data[n][self.pk]
        sql = f"UPDATE `{self.tn}` SET {fvs} WHERE `{self.pk}` = %s;"
        vl = []
        for fn in self.fields:
            if fn in self.data[n].keys():
                vl.append(self.data[n][fn])
        vl.append(idval)
        print(sql,vl)
        self.cur.execute(sql,vl)
    def deleteById(self,id):
        self.connect()
        sql = f"DELETE FROM `{self.tn}` WHERE `{self.pk}` = %s;"
        #print(sql)
        self.cur.execute(sql,(id))
