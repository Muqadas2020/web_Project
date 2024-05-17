from flask import Flask, render_template, request,make_response,session
from flask_mail import Mail, Message
from model import model
from user import user
from artist import artist
from client import client
from order import Order
import smtplib
import re

app = Flask(__name__)
app.secret_key="bsjvhusdhg5565645"
''''
app.config['MAIL_SERVER'] = "smtp.sendgrid.net"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "muqadasarshad2020@gmail.com"
app.config['MAIL_PASSWORD'] = "zyvirtspfssqeqtn"
app.config['MAIL_DEFAULT_SENDER'] = "muqadasarshad2020@gmail.com"
mail= Mail(app)
'''


'''$$$$$$$$$$$$$$$$$$$$$$$$$$ INTRO PAGE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route('/')
def FanistanIntro():
    return render_template("intro.html")
'''$$$$$$$$$$$$$$$$$$$$$$$$$$ JOIN PAGE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route('/connet-to-fanistaan')
def FanistanJoin():
    return render_template("index.html")
'''$$$$$$$$$$$$$$$$$$$$$$$$$$ BACK TO CLIENT HOME $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route("/backToHome")
def backToHome():
    return render_template("client_profile.html")

'''$$$$$$$$$$$$$$$$$$$$$$$$$$ gallery show $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route("/visitGallery")
def visitGallery():
 return render_template('fanistaan.html')
'''$$$$$$$$$$$$$$$$$$$$$$$$$$ show orders $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route("/orders")
def orders():
 dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
 user=session.get('email')
 data=dhlr.allOrders(user)
 return render_template('orders_list.html',data=data)

'''$$$$$$$$$$$$$$$$$$$$$$$$$$ LOGIN FUNCTIONALITY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route("/loginForm")
def loginForm():
 return render_template('login.html')
 



@app.route('/login', methods=['GET', 'POST'])
def login():
        try:
            email = request.form['email']
            password = request.form['password']

            # Instantiate the model class
            dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
            u1  =user(0,email,password)
            # Call the correct method for artist login
            login = dhlr.login(u1)

            print("login is: ", login[0],login[1],login[2],login[3])

            if login[3] == "ARTIST":
                ID , data =dhlr.get_ID_DATA(email)
                session["ID"] = ID
                session["email"]= email
                session["type"]="ARTIST"
                print("artist session stored")
                return render_template("artist_Profile.html")
            elif login[3] == "CLIENT" :
                ID, data=dhlr.get_ID_DATA(email)
                session["ID"] = ID
                session["email"]= email
                session["type"]="CLIENT"
                print("client session stored")
                return render_template("client_profile.html", client = data[1], message="YOU CAN NOW USE SERVICES AS ART LOVER", name= data[1])
            else:
                return render_template('login.html', error="Invalid credentials. Please try again.")

        except Exception as e:
            return render_template("login.html",error= "Invalid credentials. Please try again." )


'''$$$$$$$$$$$$$$$$$$$$$$$$$$ ARTIST SIGNUP FUNCTIONALITY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''


@app.route("/artist-signup-form")
def artist_signup_form():
 return render_template('Artist_Signup.html')

@app.route('/artist-signup', methods=['GET', 'POST'])
def artist_signup():
    valid=True
    error=None
    type='ARTIST'
    try:
            
            name = request.form['name']
            if name==None and name=='':
                valid= False
                error='User Name is requaired'

            bname = request.form['b_name']
            if bname==None and bname=='':
                valid= False
                error='Business Name is requaired'

            email = request.form['email']
            if email==None and email=='':
                valid= False
                error='Email is requaired'

            password = request.form['password']
            if password==None and password=='':
                valid= False
                error='Password is requaired'

            cpassword = request.form['cpassword']
            if cpassword==None and cpassword=='':
                valid= False
                error='Confirm Password is requaired'
            if password != cpassword:
                valid= False
                error='PASSWORD and CONFIRM PASSWORD must be SAME'

            gender = request.form['gender']
            if gender==None and gender=='':
                valid= False
                error='Gender Not Selected'

            description = request.form['bio']
            if description==None and description=='':
                valid= False
                error='The Description About You Is Mandatory. Please fill The Description Box'

            art_area=request.form['job']
            if art_area==None and art_area=='':
                valid= False
                error="No Job Selceted"
            # Instantiate the model class
            dhlr = model("localhost", "root", "Abdullah17$", "fanistan")

            art1  =artist(None,email,password,type,name,bname,email,gender,description,art_area,None,None,None)
            # Call the correct method for artist login
            signup = dhlr.ArtistsSignup(art1)
            print("signup is: ", signup)
            if valid and signup:
                return render_template("login.html")
            else:
                return render_template('Artost_Signup.html', error=error)

    except Exception as e:
            return render_template("Artost_Signup.html", error= "SignUp error: " + str(e))


'''$$$$$$$$$$$$$$$$$$$$$$$$$$ CLIENT SIGNUP FUNCTIONALITY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''


@app.route("/client-signup-form")
def client_signup_form():
 return render_template('Client_Signup.html')

@app.route('/client-signup', methods=['GET', 'POST'])
def client_signup():
    valid=True
    error=None
    type='CLIENT'
    try:
            
            name = request.form['name']
            if name==None and name=='':
                valid= False
                error='User Name is requaired'

            email = request.form['email']
            if email==None and email=='':
                valid= False
                error='Email is requaired'

            password = request.form['password']
            if password==None and password=='':
                valid= False
                error='Password is requaired'

            cpassword = request.form['cpassword']
            if cpassword==None and cpassword=='':
                valid= False
                error='Confirm Password is requaired'
            if password != cpassword:
                valid= False
                error='PASSWORD and CONFIRM PASSWORD must be SAME'

            gender = request.form['gender']
            if gender==None and gender=='':
                valid= False
                error='Gender Not Selected'

            
            # Instantiate the model class
            dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
            
            cl1 = client(None,email,password,type,name,email,gender,None,None,None)
            # Call the correct method for artist login
            signup = dhlr.ClientSignup(cl1)
            print("signup is: ", signup)
            print("valid is is: ", valid)
            if valid and signup:
                ''''
                message=('Hi! Welcome to FANISTAAN.\nYour Account has successfully registered. ')
                server=smtplib('smtp.gmail.com',587)
                server.login('muqadasarshad2020@gmail.com', 'zyvirtspfssqeqtn')   
                server.sendmail('muqadasarshad2020@gmail.com',email,message)  
                server.quit()   
                print('succeessfully')  
                '''

                return render_template("login.html")

            else:
                return render_template('Client_Signup.html', error=error)

    except Exception as e:
            return render_template("Client_Signup.html", error= "SignUp error: " + str(e))



@app.route("/search_artist_form")
def search_artist_form():
 return render_template("search_artist.html")

@app.route('/searchAnArtist', methods=['GET', 'POST'])
def search_artist():
    user=None
    user=session.get("ID")
    if user:
        try:
                name = request.form['name']
                error=None
                if name==None and name=='':
                    valid= False
                    error='YOU ENTERED NOTHING SO CANT HOLD A SEARCH'
                
                # Instantiate the model class
                dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
                
                # Call the correct method for artist login
                data = dhlr.Search_artist_UBname(name)
                print("data is  is: ", data)
                
                if data :
                    return render_template("list_artists.html",data = data)
                else:
                    return render_template('search_artist.html', error=error)

        except Exception as e:
                return render_template("Client_Signup.html", error= "SignUp error: " + str(e))
    
    else:
        return render_template("login.html", error= "TO USE THE SERVICES YOU SHOULD LOGIN 1ST")

@app.route('/searchAnArtistByID', methods=['GET', 'POST'])
def search_artist_ID():
    user=None
    user=session.get("email")
    if user:
        try:
                id = request.form['id']
                error=None
                if id==None and id=='':
                    error='YOU ENTERED NOTHING SO CANT HOLD A SEARCH'
                
                # Instantiate the model class
                dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
                
                # Call the correct method for artist login
                data = dhlr.Search_artist_ID(id)
                print("data is  is: ", data)
                
                if data :
                    return render_template("artist_Profile.html",data = data, user=user)
                else:
                    
                    return render_template('list_artists.html', error=error)

        except Exception as e:
                return render_template("list_artists.html", error= "SignUp error: " + str(e))
    
    else:
        return render_template("login.html", error= "TO USE THE SERVICES YOU SHOULD LOGIN 1ST")
    

@app.route("/toOrderForm", methods=['GET', 'POST'])
def toOrderForm():
    try:
        to=request.form['to']
        from_=request.form['from']
        return render_template("order-form.html", to=to,from_=from_)
    except Exception as e:
        return render_template("artist_Profile.html", error=str(e))
    
@app.route("/registerAnOrder", methods=['GET', 'POST'])
def registerAnOrder():
    try:
        to=request.form['to']
        from_=request.form['from_']
        des=request.form['des']
        price=request.form['price']
        time=request.form['time']
        '''
        print(urgent)
        print(str(urgent))
        print(int(urgent))
        urgent = 1 if urgent == "on" else 0
        '''
        dhlr = model("localhost", "root", "Abdullah17$", "fanistan")
        o1=Order(None,to,from_,des,price,time)
        reg =dhlr.registerOrder(o1)
        if reg: 
            msg="YOU HAVE SUCCESSFULLY PLACED THE ORDER"
            return render_template("orders_list.html",msg=msg)
        else:
            msg="FAILED TO PLACE THE ORDER"
            return render_template("orders_list.html",msg=msg)
    except Exception as e:
            
            return render_template("orders_list.html",msg=str(e))
    


@app.route('/logoutClient')
def logout(): 
    try:
        session.clear()
        return render_template("intro.html")
    except Exception as e:
        return render_template("client_profile.html", error=str(e))


app.run()