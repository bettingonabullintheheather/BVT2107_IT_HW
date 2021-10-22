# -*- coding: utf-8 -*- 
from flask import render_template 
from app import app 
 
@app.route('/') 
@app.route('/index') 
def index(): 
    user = {'username': 'Демид '} 
    posts = [ 
        { 
            'author': {'username': 'J0hn'}, 
            'body': 'i like that a lot' 
        }, 
        { 
            'author': {'username': 'xX_WebLurker_Xx'}, 
            'body': 'what a color scheme...' 
        },  
        { 
            'author': {'username': 'V4S1L17'}, 
            'body':'etot sait prosto chudo' 
        },
        { 
            'author': {'username': 'Сосед снизу'}, 
            'body':'Хватит орать про какой-то нерабочий код!' 
        } 
    ] 
    return render_template('index.html', title='Home', user=user, posts=posts)