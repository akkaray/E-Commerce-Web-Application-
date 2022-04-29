from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response
from flask_session import Session
from datetime import timedelta
import time
from users import users
from products import products
from transactions import transactions
from lineitems import lineitems
from PIL import Image
import os
from glob import glob

app = Flask(__name__,static_url_path='')

app.config['SECRET_KEY'] = '#$%34563453563$%$'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
sess = Session()
sess.init_app(app)

@app.route('/')
def home():
    return redirect('/login')


@app.route('/selectProd',methods=['GET','POST'])
def selectProd():
    return render_template('selectProd.html')

@app.route('/selectShip',methods=['GET','POST'])
def selectShip():
    product = request.form.get('product')
    session['product'] = product
    return render_template('selectShip.html',product=product)

@app.route('/confirm',methods=['GET','POST'])
def confirm():
    #product = request.form.get('product')
    product = session['product']
    ship = request.form.get('ship')
    return render_template('confirm.html',product=product,ship=ship)




@app.route('/set')
def set():
    session['key'] = 'value'
    session['time'] = time.time()
    return 'ok'

@app.route('/get')
def get():
    return str(session.get('time', 'not set'))

@app.route('/test')
def test():
    user = 'Tommy'
    return render_template('test.html',username = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = 'Welcome'
    if request.form.get('username') is not None:
        u=users()
        if u.trylogin(request.form.get('username'), request.form.get('pw')):
            session['user'] = u.data[0]
            session['last_login'] = time.time()
            return redirect('/main_menu')
        else:
            msg = 'Login failed'

    return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session['user'] = None 
    return render_template('logout.html')

#display form
@app.route('/enterName')
def enterName():
    return render_template('nameForm.html')

#process form
@app.route('/submitName',methods=['GET','POST'])
def submitName():
    username = request.form.get('myname')
    othername = request.form.get('othername')
    print(othername)
    print(username)
    #At this point we would INSERT the user's name to the mysql table
    return render_template('message.html',msg='name '+str(username)+' added!')


@app.route('/submitNameGet',methods=['GET','POST'])
def submitNameGet():
    username = request.args.get('myname')
    print(username)
    #At this point we would INSERT the user's name to the mysql table
    return render_template('message.html',msg='name '+str(username)+' added!')

@app.route('/elements')
def elements():
    return render_template('formelements.html')



@app.route('/register')
def register():
    account = 'jan@aol.com'
    return render_template('myregistration.html',account = user_account)



# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/main_menu',methods=['GET','POST'])
def main_menu():
    u=users()
    if userType() == "employee":
        if userType() != False:    
            print(session.get('user'))
            return render_template('main_menu.html',me = session.get('user'))
        else:
            return redirect('/login')
    else:
        if userType() != False:    
            print(session.get('user'))
            return render_template('main_menu_customer.html',me = session.get('user'))
        else:
            return redirect('/login')
    
    
    
@app.route('/users',methods=['GET','POST'])
def list():
    if userType() != False: 
        print(request.args.get('id'))
        u = users()
        if request.args.get('task') == 'delete':
            u.deleteById(request.args.get('id'))
        if request.args.get('task') == 'add':
            d = {}
            d['fname'] = request.form.get('fname')
            d['lname'] = request.form.get('lname')
            d['email'] = request.form.get('email')
            d['pw'] = request.form.get('pw')
            d['type'] = request.form.get('type')
            d['age'] = request.form.get('age')
            d['gender'] = request.form.get('gender')
            u.add(d)
            print(u.data)
            if u.verify_new():
                print(u.data)
                u.insert()
            else:
                print(u.errors)
                return render_template('users/add.html',object = u)
            
        if request.args.get('task') == 'update':
            u.getById(request.args.get('id'))
            u.data[0]['fname'] = request.form.get('fname')
            u.data[0]['lname'] = request.form.get('lname')
            u.data[0]['email'] = request.form.get('email')
            u.data[0]['type'] = request.form.get('type')
            u.data[0]['age'] = request.form.get(age)
            u.data[0]['gender'] = request.form.get('gender')
            if u.verify_update():
                u.update()
            else:
                return render_template('users/edit.html',object = u)
            
        if request.args.get('id') is not None and request.args.get('task') is None:
            if request.args.get('id') == 'add':
                u.create_blank()
                return render_template('users/add.html',object = u)
            else:
                u.getById(request.args.get('id'))
                print(u.data)
                return render_template('users/edit.html',object = u)
        else:
            u.getAll()
            #print(u.data)
            return render_template('users/list.html',table = u)
    else:
        return redirect('/login')

def userType():
    if session.get('user') is None:
        return False
    else:
        return session.get('user')['type']
        
@app.route('/products',methods=['GET','POST'])
def Productlist():
    if userType() != False and userType()=='employee': 
        print(request.args.get('ProductId'))

        o = products()
        if request.args.get('task') == 'delete':
            o.deleteById(request.args.get('ProductId'))
        if request.args.get('task') == 'add':
            d = {}
            d['PType'] = request.form.get('PType')
            d['PColor'] = request.form.get('PColor')
            d['PSize'] = request.form.get('PSize')
            d['PBrand'] = request.form.get('PBrand')
            d['PPrice'] = request.form.get('PPrice')
            d['PName'] = request.form.get('PName')
            d['img'] = request.form.get('img')
            
            o.add(d)
            print(o.data)
            if o.verify_new():
                print(o.data)
                o.insert()
            else:
                print(o.errors)
                return render_template('products/add.html',object = o)
            
        if request.args.get('task') == 'update':
            o.getById(request.args.get('ProductId'))
            o.data[0]['PType'] = request.form.get('PType')
            o.data[0]['PColor'] = request.form.get('PColor')
            o.data[0]['PSize'] = request.form.get('PSize')
            o.data[0]['PBrand'] = request.form.get('PBrand')
            o.data[0]['PPrice'] = request.form.get('PPrice')
            o.data[0]['PName'] = request.form.get('PName')
            o.data[0]['img'] = request.form.get('img')
            if o.verify_update():
                o.update()
            else:
                return render_template('products/edit.html',object = o)
        if request.args.get('task') == 'view':
            o.getAll(request.args.get('ProductId'))
            return render_template('products/view.html',table = o)
            
        if request.args.get('ProductId') is not None and request.args.get('task') is None:
            if request.args.get('ProductId') == 'add':
                o.create_blank()
                return render_template('products/add.html',object = o)
            else:
                o.getById(request.args.get('ProductId'))
                print(o.data)
                return render_template('products/edit.html',object = o)
        else:
            
            o.getAll()
            #print(o.data)
            return render_template('products/listemployee.html',table = o)
    else:
        o=products()
        o.getAll()
            #print(o.data)
        return render_template('products/listcustomer.html',table = o)
        
        
@app.route('/transactions',methods=['GET','POST'])
def transactionslist():
    if userType() != False: 
        print(request.args.get('TId'))
        o = transactions()
        o.getopenTId()
        
    else:
        return redirect('/login')   
        
@app.route('/lineitems',methods=['GET','POST'])
def lineitemslist():
    if userType() != False: 
        print(request.args.get('lineitemId'))
        t=transactions()
        TId =t.getopenTId(session.get('user')['id'])
        o = lineitems()
        p=products()
        p.getAll()
        o.products=p.data
        if request.args.get('task') == 'delete':
            o.deleteById(request.args.get('lineitemId'))
        if request.args.get('task') == 'add':
            d = {}
            d['Quantity'] = request.form.get('Quantity')
            d['ProductId'] = request.form.get('ProductId')
            d['TId'] = TId
            o.add(d)
            print(o.data)
            
            o.insert()
               
        if request.args.get('task') == 'update':
            o.getById(request.args.get('lineitemId'))
            o.data[0]['Quantity'] = request.form.get('Quantity')
            o.data[0]['TId'] = TId
            
            if o.verify_update():
                o.update()
            else:
                return render_template('lineitems/edit.html',object = o)
            
        if request.args.get('lineitemId') is not None and request.args.get('task') is None:
            if request.args.get('lineitemId') == 'add':
                o.create_blank()
                return render_template('lineitems/add.html',object = o)
            else:
                o.getById(request.args.get('lineitemId'))
                print(o.data)
                return render_template('lineitems/edit.html',object = o)
        else:
            o.getTId(TId)
            #print(o.data)
            return render_template('lineitems/list.html',table = o)
    else:
        return redirect('/login')
        
@app.route('/checkout',methods=['GET','POST'])
def checkoutlist():
    if userType() != False: 
        print(request.args.get('lineitemId'))
        t=transactions()
        TId =t.getopenTId(session.get('user')['id'])
        l=lineitems()
        l.getTId(TId)
        print(l.data)
        total=l.getTotal()
        print(total)
        if request.args.get('task')=='confirm':
            t.getById(TId)
            t.data[0]['Tstatus']='placed'
            t.data[0]['Paymenttype']=request.form.get('type')
            t.data[0]['Amount']=total
            t.update()
            l.transactions=t.data
            return render_template('checkout/checkout.html',object = l) 
        return render_template('checkout/edit.html',object = l)
        
    else:
        return redirect('/login')
         
         
         
@app.route('/checkoutcomplete',methods=['GET','POST'])
def checkout():
    if request.args.get('task')=='complete': 
            return render_template('checkout/checkoutcomplete.html')
    
    

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
