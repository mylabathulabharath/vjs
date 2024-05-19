from flask import Flask, render_template, request, session,redirect,url_for
import sqlite3
import random
from twilio.rest import Client
import requests
import requests
import certifi

response = requests.get('https://api.twilio.com/2010-04-01/Accounts/AC439e4b0f77fd727a91356843af773d4a/Messages.json', verify=certifi.where())
print(response)


app=Flask(__name__)
app.secret_key='123456qwerty'

sid="AC439e4b0f77fd727a91356843af773d4a"
token='f22fe062ef8f700754b44eca96baa5d5'
my_num="+16592668431"



@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        phone=request.form['phone']
        conn=create_connection()
        cur=conn.cursor()
        cur.execute('''SELECT * FROM VJS WHERE USERNAME=? AND PASSWORD=?''',(username,password))
        data=cur.fetchone()
        conn.commit()
        conn.close() 
        print(data)
        if data:
            otp=generate_otp()
            session['otp']=otp
            client=Client(sid,token)
            message=client.messages.create(
            body=otp,
            from_=my_num,
            to='+919381666049'
            )
            print(message)
            return render_template('otppage.html')
        else:
            return "Wrong credentials"
    return render_template('index.html')

@app.route('/otp', methods=['GET','POST'])
def otpvalidate():
    if request.method=='POST':
        otp_user=request.form['otp']
        if otp_user == str(session['otp']):
            return render_template('home.html')
        else:
            return "Wrong OTP"
    return render_template('otppage.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method=='POST':
        uname=request.form['username']
        pswd=request.form['password']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO VJS (USERNAME,PASSWORD) VALUES(?,?)''',(uname,pswd))
        conn.commit()
        conn.close()
        return render_template('index.html')
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/palnadu')
def palnadu():
    return render_template('palnadu.html')
@app.route('/nandyal')
def nandyal():
    return render_template('nandyal.html')
@app.route('/prakasham')
def prakasham():
    return render_template('prakasham.html')
@app.route('/nellore')
def nellore():
    return render_template('nellore.html')
@app.route('/bapatla')
def bapatla():
    return render_template('bapatla.html')
@app.route('/srikakulam')
def srikakulam():
    return render_template('srikakulam.html')
@app.route('/vizianagaram')
def vizianagaram():
    return render_template('vizianagaram.html')
@app.route('/manyam')
def manyam():
    return render_template('manyam.html')
@app.route('/ananthapuram')
def ananthapuram():
    return render_template('ananthapuram.html')
@app.route('/eastgodavari')
def eastgodavari():
    return render_template('eastgodavari.html')
@app.route('/konaseema')
def konaseema():
    return render_template('konaseema.html')
@app.route('/kakinada')
def kakinada():
    return render_template('kakinada.html')
@app.route('/kadapa')
def kadapa():
    return render_template('kadapa.html')
@app.route('/vizag')
def vizag():
    return render_template('vizag.html')
@app.route('/chittoor')
def chittoor():
    return render_template('chittoor.html')
@app.route('/tirupati')
def tirupati():
    return render_template('tirupati.html')
@app.route('/ntr')
def ntr():
    return render_template('ntr.html')
@app.route('/guntur')
def guntur():
    return render_template('guntur.html')
@app.route('/kurnool')
def kurnool():
    return render_template('kurnool.html')
@app.route('/annamayya')
def annamayya():
    return render_template('annamayya.html')
@app.route('/eluru')
def eluru():
    return render_template('eluru.html')
@app.route('/westgodavari')
def westgodavari():
    return render_template('westgodavari.html')
@app.route('/krishna')
def krishna():
    return render_template('krishna.html')
@app.route('/allurisitaramaraju')
def allurisitaramaraju():
    return render_template('allurisitaramaraju.html')
def create_connection():
    conn=sqlite3.connect('user3.db')
    return conn
def create_table():
    conn=create_connection()
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS VJS(USERNAME VARCHAR(50) NOT NULL,PASSWORD VARCHAR(6) NOT NULL)")
    conn.commit()
    conn.close()

def generate_otp():
    res=random.randint(100000,999999)
    return res

if __name__=='__main__':
    create_table()
    generate_otp()
    app.run(host='0.0.0.0', port=8080)
