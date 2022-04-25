from users import users
u = users()
print(u.trylogin('b@b.com', '123'))
print(u.data)
print(u.trylogin(' ', '123'))

#print(u.fields, u.pk)
'''
d = {}
d['fname'] = 'test'
d['lname'] = 'user_lname'
d['email'] = 'test@test.com'
d['pw'] = '123'
d['type'] = '1'
u.add(d)
u.insert()
u.getAll()
print(u.data)

u.getById(3)
u.data[0]['lname'] = "NewName"
u.data[0]['fname'] = "NewName12345"
#print(u.data)
u.update()
u.deleteById(8)
'''
