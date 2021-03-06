# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import LoginForm
from pick import *

@app.route('/')
@app.route('/index')
def index(alias = 'GUEST'):
    return render_template("index.html", title = "Home")

@app.route('/food')
def food():
    return render_template("food.html", title = "Food")

@app.route('/result', methods = ['GET'])
def showFoodResult():
    locations = request.args.getlist('Location')
    if len(locations) == 0:
        return render_template("food.html", title = "Food")
    else:
        choice, number = pick_food(locations)
        return render_template("food_result.html", title=u"Picked!", choice=choice.decode('utf-8'), number=number)

@app.route('/activity')
def activity():
    activity = pick_activity()
    return render_template("activity.html", title = "Activity picked!", activity = activity.decode('utf-8'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Amazon alias = "%s", remember_me = %s' %
              (form.user.data, str(form.remember_me.data)))
        return render_template("index.html", title='Home', alias=form.user.data)
    return render_template('login.html',  title='Sign In', form=form)