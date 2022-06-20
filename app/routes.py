from app import app #means to get the app flask intance from the /app package
#from flask import render_template, jsonify #what other flask things do we need ?
from flask import render_template, flash, redirect, url_for, request, jsonify, \
make_response, session, Response, send_from_directory, send_file
import requests
import json #why is this not in the requirements.txt file ???
#how do we get Jinja2?
import datetime


# ------------------------------- GLOBAL VARIABLES --------------------------

API_URL = app.config['API_ROUTE']
# RECAPTCHA_SITE_KEY = app.config['RECAPTCHA_SITE_KEY']

# ------------------------------- GLOBAL VARIABLES --------------------------

# ------------------------------- HELPER FUNCTIONS --------------------------

# @app.before_request
# def before_request():
#     if app.config['FLASK_CONFIG'] == 'heroku' and not request.is_secure:
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)
        
# ------------------------------- HELPER FUNCTIONS --------------------------


@app.route('/')
@app.route('/index')
@app.route('/light_mode')
def light_mode():

    r_awards = requests.get(API_URL+'/get_awards')

    if(r_awards.status_code == 200):
        print("succeeded getting the awards from the API")
        awards = r_awards.json()
        print("awards : ", awards)

    r_certifications = requests.get(API_URL+'/get_certifications')

    if(r_certifications.status_code == 200):
        print("succeeded getting the certifications from the API")
        certifications = r_certifications.json()
        print("certifications : ", certifications)

    r_programming_tools = requests.get(API_URL+'/get_programming_tools')

    if(r_programming_tools.status_code == 200):
        print("succeeded getting the programmingtools from the API")
        programmingtools = r_programming_tools.json()
        print("programmingtools : ", programmingtools)

    r_work_experiences = requests.get(API_URL+'/get_work_experiences')

    if(r_work_experiences.status_code == 200):
        print("succeeded getting the workexperiences from the API")
        workexperiences = r_work_experiences.json()
        print("workexperiences : ", workexperiences)

    return render_template('light_mode/light_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")

@app.route('/dark_mode')
def dark_mode():

    r_awards = requests.get(API_URL+'/get_awards')

    if(r_awards.status_code == 200):
        print("succeeded getting the awards from the API")
        awards = r_awards.json()
        print("awards : ", awards)

    r_certifications = requests.get(API_URL+'/get_certifications')

    if(r_certifications.status_code == 200):
        print("succeeded getting the certifications from the API")
        certifications = r_certifications.json()
        print("certifications : ", certifications)

    r_programming_tools = requests.get(API_URL+'/get_programming_tools')

    if(r_programming_tools.status_code == 200):
        print("succeeded getting the programmingtools from the API")
        programmingtools = r_programming_tools.json()
        print("programmingtools : ", programmingtools)

    r_work_experiences = requests.get(API_URL+'/get_work_experiences')

    if(r_work_experiences.status_code == 200):
        print("succeeded getting the workexperiences from the API")
        workexperiences = r_work_experiences.json()
        print("workexperiences : ", workexperiences)

    return render_template('dark_mode/dark_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")