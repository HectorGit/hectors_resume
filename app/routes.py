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

    with open('./app/static/js/temporary_json_files/certifications.json', 'r') as certifications_file_pointer:
        certifications = json.load(certifications_file_pointer)['certifications']
        # print("\n CERTIFICATIONS : ", certifications)

    with open('./app/static/js/temporary_json_files/programming_tools.json', 'r') as programming_tools_file_pointer:
        programmingtools = json.load(programming_tools_file_pointer)['programming_tools']
        # print("\n PROGRAMMING TOOLS :", programmingtools)

    with open('./app/static/js/temporary_json_files/work_experiences.json', 'r') as work_experiences_file_pointer:
        workexperiences = json.load(work_experiences_file_pointer)['work_experiences']
        # print("\n WORK EXPERIENCES:", workexperiences)

    return render_template('light_mode/light_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")

@app.route('/dark_mode')
def dark_mode():

    r_awards = requests.get(API_URL+'/get_awards')

    if(r_awards.status_code == 200):
        print("succeeded getting the awards from the API")
        awards = r_awards.json()
        print("awards : ", awards)

    with open('./app/static/js/temporary_json_files/certifications.json', 'r') as certifications_file_pointer:
        certifications = json.load(certifications_file_pointer)['certifications']
        # print("\n CERTIFICATIONS : ", certifications)

    with open('./app/static/js/temporary_json_files/programming_tools.json', 'r') as programming_tools_file_pointer:
        programmingtools = json.load(programming_tools_file_pointer)['programming_tools']
        # print("\n PROGRAMMING TOOLS :", programmingtools)

    with open('./app/static/js/temporary_json_files/work_experiences.json', 'r') as work_experiences_file_pointer:
        workexperiences = json.load(work_experiences_file_pointer)['work_experiences']
        # print("\n WORK EXPERIENCES:", workexperiences)

    return render_template('dark_mode/dark_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")