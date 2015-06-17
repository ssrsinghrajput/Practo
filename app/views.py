from flask import render_template, flash, redirect, jsonify, request, url_for
from app import app, models, db
from jinja2 import Environment, PackageLoader
import json

env = Environment(loader=PackageLoader('app', "templates"))
basic_template = env.get_template('basic_template.html')
search_template = env.get_template('search_template.html')
city_template = env.get_template('city_template.html')

@app.route("/")
def home_page():
    practoCSS = url_for('static', filename='practo.css')
    functionsJS = url_for('static', filename='city.js')
    return city_template.render(practoCSS=practoCSS, functionsJS=functionsJS)

@app.route("/<city>")
def search_page(city,index=1):

    practoCSS = url_for('static', filename='practo.css')
    functionsJS = url_for('static', filename='functions.js')
    return search_template.render(practoCSS=practoCSS, functionsJS=functionsJS, city=city, index=index)

@app.route("/get/<city>")
def areas_by_city(city):
        list = models.AreaMapping.query.filter_by(city=city)
        areas = []
        for li in list:
            m = {}
            for key in li.__dict__.keys():
                if key != '_sa_instance_state':
                    m[key] = li.__dict__[key]
            areas.append(m)
        return jsonify(results=areas)

@app.route('/<city>/<area>/<specialization>/<page>',methods=['GET', 'POST'])
def doctors_by_area(city, area, specialization, page):
    list = models.Doctor.query.filter_by(
        city=city, area=area, specialization=specialization)
    list_of_doctors = []
    counter = 0
    low = 10*(int(page)-1)
    high = 10*(int(page)) - 1
    for li in list:
        m = {}
        if counter >= low and counter <= high:
            for key in li.__dict__.keys():
                if key != '_sa_instance_state':
                    m[key] = li.__dict__[key]
            list_of_doctors.append(m)
        counter += 1
    return jsonify(results=list_of_doctors)



@app.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit_doctor(user_id):
    if request.method == "POST":
        u = models.Doctor.query.filter_by(id=user_id).first()
        u.name = request.form['name']
        db.session.commit()
        return redirect('edit.html')
    else:
        return render_template('edit.html')


@app.route('/add_area', methods=['GET', 'POST'])
def add_area():
    if request.method == "POST":
        print request.form['area']
        u = models.AreaMapping(request.form['area'], request.form['city'])
        db.session.add(u)
        db.session.commit()
        return render_template('add_new.html')
    else:
        return render_template('add_new.html')


@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == "POST":
        u = models.Doctor(request.form['name'], request.form['education'], request.form['expertise'], request.form['experience'], request.form['email'], request.form['description'], request.form[
            'specialization'], request.form['area'], request.form['city'], request.form['country'], request.form['completeaddress'], request.form['fee'], request.form['phone_number'], request.form['timings'])
        db.session.add(u)
        db.session.commit()
        return render_template('add_doctor.html')
    else:
        return render_template('add_doctor.html')


@app.route('/doctors/<city>')
def doctors_by_city(city):
    list = models.Doctor.query.filter_by(city=city)
    L = []
    for li in list:
        m = {}
        for key in li.__dict__.keys():
            if key != '_sa_instance_state':
                m[key] = li.__dict__[key]
        L.append(m)
    print L
    return jsonify(results=L)
