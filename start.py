from flask import Flask
from flask import render_template
from flask import request
import requests
import json

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['post'])

def organization():
    payload = {'apikey':'VdEDyf9zyAwExmja9hnTKluuVkaKUAIx'} #your API key
    us=request.form['uname']
    pwd=request.form['pwd']
    user_auth = (us, pwd)
    res = requests.get('https://services.adroll.com/api/v1/organization/get', params=payload, auth=user_auth)
    org_details = res.content
    return render_template('org.html',org=org_details)



if __name__ == '__main__':
    app.run(debug=True)
