from app import app #means to get the app flask intance from the /app package
#from flask import render_template, jsonify #what other flask things do we need ?
from flask import render_template, flash, redirect, url_for, request, jsonify, \
make_response, session, Response
import requests
import json #why is this not in the requirements.txt file ???
#how do we get Jinja2?

# ------------------------------- GLOBAL VARIABLES --------------------------

API_URL = app.config['API_ROUTE']

# ------------------------------- GLOBAL VARIABLES --------------------------

# Called from contact.js
# In charge of making the call to the API and returning whether it was successful or not . 
@app.route('/ajax_send_email', methods=['POST'])
def ajax_send_email():

    print("request.form : \n ")
    print(request.form['first_name'])
    print(request.form['last_name'])
    print(request.form['subject'])
    print(request.form['inquirer_email'])
    print(request.form['message'])

    print('reached AJAX HANDLERS /ajax_send_email')

    url = API_URL + '/send_email'

    print('url: ', url)

    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "subject":request.form['subject'],
        "inquirer_email" : request.form["inquirer_email"],
        "message":request.form['message']
    }

    r1 = requests.post(url, data=data)

    if r1.status_code == 200:
        return json.dumps({'success': True})
    else :
        return json.dumps({'success': False})

@app.route('/ajax_validate_captcha', methods=['POST'])
def ajax_validate_captcha():

    url = API_URL + "/api_validate_captcha"

    data = {
        'g_recaptcha_response': request.form['g_recaptcha_response']
    }

    print('about to call /api_validate_captcha - url : \n', url)
    print('\n about to call /api_validate_captcha - data : \n', data )

    r = requests.post(url, data = data)

    print(r) #<Response [###]>

    if r.status_code == 200:
        print('/api_validate_captcha succeeded ')
        recaptcha_response = r.json()
        print('response json: ', recaptcha_response)
        return json.dumps({'success': True , 'recaptcha_response' : recaptcha_response})
    else :
        print('/api_validate_captcha failed ')
        return json.dumps({'success': False})
