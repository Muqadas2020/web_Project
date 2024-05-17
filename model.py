from user import user
from artist import artist
from client import client
import mysql
import mysql.connector

class model:
    def __init__(self,host=None,user=None,password=None,database=None):
        self.host=host
        self.user = user
        self.password=password
        self.database=database

    def get_ID_DATA(self,email):
        mydb = None
        cursor=None
        ID = None
        data=None
        try:
            mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            sql = "select * from user where email = %s"
            args = (email,)
            cursor.execute(sql, args)
            print("into get id Got Id")
            check = cursor.fetchone()

            if check:
                if check[3]=='ARTIST':
                    sql = "select * from artist where email = %s"
                    args = (email,)
                    cursor.execute(sql, args)
                    print("into get id Got artist")
                    data = cursor.fetchone()
                    ID=int(check[0])
                    print(ID)
                elif check[3]=='CLIENT':
                    sql = "select * from client where email = %s"
                    args = (email,)
                    cursor.execute(sql, args)
                    print("into get id Got artist")
                    data = cursor.fetchone()
                    ID=int(check[0])
                    print(ID)
            else:
                ID=None
                data=None

        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()

            if mydb != None:
                mydb.close()
            return  ID, data

    def login(self,user):
        conn = None
        curs = None
        login = None

        try:
            conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = conn.cursor()
            print("got conn and cursor ")
            query = "SELECT * FROM user WHERE email=%s AND password=%s"
            args = (user.email, user.password)
            curs.execute(query, args)
            login = curs.fetchone()
            print("login in model is: ", login)
        except Exception as e:
            conn.rollback()
            print("in model Error occurred while logging in :", e)
            print(str(e))
            login=None
        finally:
            if curs != None:
                curs.close()
            if conn != None:
                conn.close()
            return login
        

    




    def ArtistsSignup(self,artist):
        conn = None
        curs = None
        chk=False
        signup = False

        try:
            print("into check part of insert")
            conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = conn.cursor()
            print("got conn and cursor ")
            query = "SELECT * FROM user WHERE email=%s AND password=%s"
            args = (artist.email, artist.password)
            curs.execute(query, args)
            chk = curs.fetchone()
            print("ye mila chk ko: ", chk)
            if chk:
                signup=False
                print("user already ha")
            else:
                print("user user nai ha insert kro ab")
                query = "INSERT INTO user (email,password,type) VALUES (%s,%s,%s)"
                args = (artist.email, artist.password,artist.type)
                curs.execute(query, args)
                print("inserted user")
                query = "INSERT INTO artist (email,uname,bname,gender,description,art_area) VALUES (%s,%s,%s,%s,%s,%s)"
                args = (artist.email, artist.name,artist.bname,artist.gender,artist.description,artist.job)
                curs.execute(query, args)
                
                conn.commit()
                print("inserted artist")
                signup = True
        except Exception as e:
            conn.rollback()
            print("in model Error occurred while signup  :", e)
            print(str(e))
            signup = False
        finally:
            if curs != None:
                curs.close()
            if conn != None:
                conn.close()
            return signup
        

    def ClientSignup(self,client):
        conn = None
        curs = None
        chk=False
        signup = False

        try:
            print("into check part of insert")
            conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = conn.cursor()
            print("got conn and cursor ")
            query = "SELECT * FROM user WHERE email=%s AND password=%s"
            args = (client.email, client.password)
            curs.execute(query, args)
            chk = curs.fetchone()
            print("ye mila chk ko: ", chk)
            if chk:
                signup=False
                print("user already ha")
            else:
                print("user user nai ha insert kro ab")
                query = "INSERT INTO user (email,password,type) VALUES (%s,%s,%s)"
                args = (client.email, client.password,client.type)
                curs.execute(query, args)
                print("inserted user")
                query = "INSERT INTO client (name,email,gender) VALUES (%s,%s,%s)"
                args = (client.name, client.email,client.gender)
                curs.execute(query, args)
                
                conn.commit()
                print("inserted client")
                signup = True
        except Exception as e:
            conn.rollback()
            print("in model Error occurred while signup client  :", e)
            print(str(e))
            signup = False
        finally:
            if curs != None:
                curs.close()
            if conn != None:
                conn.close()
            return signup
        
    def Search_artist_UBname(self,name):
        print('INTIOOOOO search by uname and bname')
        mydb = None
        cursor=None
        data = None
        name=('%'+name+'%')
        try:
            # Get DB Connection
            mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = mydb.cursor()
            sql = "select * from artist where LOWER(uname) like LOWER(%s) or LOWER(bname) like LOWER(%s) "
            args = (name,name)
            cursor.execute(sql, args)
            data = cursor.fetchall()
            print("got all artists data")
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()

            if mydb != None:
                mydb.close()
            print("returning data")
            return  data
        

    def Search_artist_ID(self,id):
        print('INTIOOOOO search by uname and bname')
        mydb = None
        cursor=None
        data = None
        try:
            # Get DB Connection
            mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = mydb.cursor()
            sql = "select * from artist where id = %s "
            args = (id,)
            cursor.execute(sql, args)
            data = cursor.fetchone()
            print("got all artists data")
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()

            if mydb != None:
                mydb.close()
            print("returning data")
            return  data


    def registerOrder(self,o1):
        conn = None
        curs = None
        chk=False
        reg = False

        try:
            print("into check part of insert")
            conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = conn.cursor()
            print("got conn and cursor ")
            query = "SELECT * FROM orders WHERE to_user=%s AND from_user=%s"
            args = (o1.to, o1.from_)
            curs.execute(query, args)
            chk = curs.fetchall()
            print("ye mila chk ko: ", chk)
            if len(chk)>=3:
                reg=False
            else:
                print("user user nai ha insert kro ab")
                query = "INSERT INTO orders (to_user,from_user,description,price,time) VALUES (%s,%s,%s,%s,%s)"
                args = (o1.to,o1.from_,o1.des,o1.price,o1.time )
                curs.execute(query, args)
                conn.commit()
                print("inserted order")
                reg = True
        except Exception as e:
            conn.rollback()
            print("in model Error occurred while signup client  :", e)
            print(str(e))
            reg = False
        finally:
            if curs != None:
                curs.close()
            if conn != None:
                conn.close()
            return reg

    def allOrders(self,user):
        conn = None
        curs = None
        all = None

        try:
            
            conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = conn.cursor()
            query = "SELECT * FROM orders where from_user=%s"
            args = (user, )
            curs.execute(query, args)
            all=curs.fetchall()
            print("selected")
        except Exception as e:
            conn.rollback()
            print("in model Error occurred while signup client  :", e)
            print(str(e))
            all = None
        finally:
            if curs != None:
                curs.close()
            if conn != None:
                conn.close()
            return all








