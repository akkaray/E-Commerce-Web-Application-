from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response
from flask_session import Session
from datetime import timedelta
import time
from users import users

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
        if u.trylogin(request.form.get('username'), request.form.get('password')):
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
    if userType() != False:    
        print(session.get('user'))
        return render_template('main_menu.html',me = session.get('user'))
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
            u.add(d)
            u.insert()
        if request.args.get('task') == 'update':
            u.getById(request.args.get('id'))
            u.data[0]['fname'] = request.form.get('fname')
            u.data[0]['lname'] = request.form.get('lname')
            u.data[0]['email'] = request.form.get('email')
            u.data[0]['type'] = request.form.get('type')
            u.update()
        if request.args.get('id') is not None and request.args.get('task') is None:
            if request.args.get('id') == 'add':
                return render_template('users/add.html',object = u.data)
            else:
                u.getById(request.args.get('id'))
                print(u.data)
                return render_template('users/edit.html',object = u.data)
        else:
            u.getAll()
            #print(u.data)
            return render_template('users/list.html',table = u.data)
    else:
        return redirect('/login')

def userType():
    if session.get('user') is None:
        return False
    else:
        return session.get('user')['type']



if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
