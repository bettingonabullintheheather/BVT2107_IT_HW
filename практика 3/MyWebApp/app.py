import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db1",
                        user="postgres",
                        password="21082003",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        if request.form.get("login"):
            return redirect("/login/")
        elif request.form.get("registration"):
            return redirect("/registration/")     
    return render_template('main.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username') 
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            if records ==[]:
                return render_template('error.html')
            return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
        elif request.form.get("registration"):
            return redirect("/registration/")
    return render_template('login.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
  
        if len(name) < 3:   
            print('Invalid name.')
            while len(name) < 3:
                name = request.form.get('name')
        if len(login) < 3:   
            print('Invalid login.')
            while len(login) < 3:
                login = request.form.get('login')   
        if len(password) < 6:   
            print('Invalid password.')
            while len(password) < 6:
                password = request.form.get('password') 

        cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()
        return redirect('/login/')

    return render_template('registration.html')