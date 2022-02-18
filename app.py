from flask import Flask,render_template,url_for,redirect,session,make_response
import mysql.connector as mysql
from flask import request
import os


app=Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/connect')
def contact():
    return render_template("ContactUs.html")    


@app.route('/service')
def service():
    return render_template("services.html")


@app.route('/donate')
def donate():
    return render_template("donate.html")  


@app.route('/thankyou')
def thanks():
    return render_template("thanks.html") 

@app.route('/payment',methods=['POST'])
def pay():
       
    return render_template("thanks.html")      
    
if __name__=="__main__":
  app.run(debug=True)   