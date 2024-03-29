from app import app #means to get the app flask intance from the /app package
#from flask import render_template, jsonify #what other flask things do we need ?
from flask import render_template, flash, redirect, url_for, request, jsonify, \
make_response, session, Response, send_from_directory, send_file
import requests
import json #why is this not in the requirements.txt file ???
#how do we get Jinja2?
import datetime


# ------------------------------- GLOBAL VARIABLES --------------------------

# DEACTIVATED
# API_URL = app.config['API_ROUTE']
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

@app.route('/light_mode')
def light_mode():

    # awards = fetch_awards()
    # certifications = fetch_certifications()
    # programmingtools = fetch_programming_tools()
    # workexperiences = fetch_work_experiences()

    return render_template('light_mode/light_mode.html', title="Hector Perez")
    # return render_template('light_mode/light_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")

@app.route('/')
@app.route('/index')
@app.route('/dark_mode')
def dark_mode():

    # awards = fetch_awards()
    # certifications = fetch_certifications()
    # programmingtools = fetch_programming_tools()
    # workexperiences = fetch_work_experiences()

    return render_template('dark_mode/dark_mode.html', title="Hector Perez")
    # return render_template('dark_mode/dark_mode.html', awards=awards, certifications=certifications, programmingtools=programmingtools, workexperiences=workexperiences, title="Hector Perez")

# DEACTIVATED
# def fetch_awards(): 
#     awards = []
#     r_awards = requests.get(API_URL+'/get_awards')
#     if(r_awards.status_code == 200):
#         awards = r_awards.json()
#     return awards

# DEACTIVATED
# def fetch_certifications(): 
#     certifications = []
#     r_certifications = requests.get(API_URL+'/get_certifications')
#     if(r_certifications.status_code == 200):
#         certifications = r_certifications.json()
#     return certifications

# DEACTIVATED
# def fetch_programming_tools():
#     programmingtools = []
#     r_programming_tools = requests.get(API_URL+'/get_programming_tools')
#     if(r_programming_tools.status_code == 200):
#         programmingtools = r_programming_tools.json()
#     return programmingtools

# DEACTIVATED
# def fetch_work_experiences():

#     workexperiences = []

#     r_work_experiences = requests.get(API_URL+'/get_work_experiences')

#     if(r_work_experiences.status_code == 200):
#         workexperiences = r_work_experiences.json()
#         for workexperience in workexperiences:
#             # if it has projects
#             if workexperience['projects_key'] is not None:
#                 fetch_work_experience_projects(workexperience)

#     return workexperiences

# def fetch_work_experience_projects(workexperience):
#     #fetch the projects
#     r_work_experiences_projects = requests.get(API_URL+'/get_work_experience_projects/'+workexperience['projects_key'])
#     # and , on success
#     if(r_work_experiences_projects.status_code==200):
#         #append the projects to the workexperience 
#         projects_retrieved = r_work_experiences_projects.json()
#         workexperience['projects'] = projects_retrieved
#     return
