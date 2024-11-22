# Oauth2System

OAuth2System - a simple authorization system for multiple sites or projects.

# Quick Start Demo

First, you need to [register an account](https://emeraldermine.onpella.app/registration), and also [confirm your email](https://emeraldermine.onpella.app/account/email_confirm). [Here](https://emeraldermine.onpella.app/apps) you can create your first application. After that, you will receive a CLIENT ID and a CLIENT SECRET. You'll need them later.
This is the authorization link - https://emeraldermine.onpella.app/oauth2/authorize?client_id={YOUR_CLIENT_ID}&scope={permissions} (in the "scope" value, you must insert the values that the system receives.) 
For example, identify - access to username, display name, user id and avatar, and email to email. If you want to add 2 values at once, then specify something like "identify+email". 
After successful authorization, the user will be redirected to the link you specified in the redirect uri field with the ending "?code={random_code}". You can get the value "code" and already using it and client id and client secret you can get the user using the API.

# API USAGE

And so, to get a user, you need to use this link "emeraldermine.onpella.app/api/user?oauth_token={OAUTH_TOKEN}&client_id={YOUR_CLIENT_ID}&client_secret={YOUR_CLIENT_SECRET}".


## The simple example

The following example will be shown based on a site created in [Python](https://www.python.org) - [Flask](https://pypi.org/project/Flask/).

```python
from flask import Flask, render_template, request, session, redirect, url_for
import requests

DOMAIN = "https://emeraldermine.onpella.app"

CLIENT_ID = 000
CLIENT_SECRET = '...'

app = Flask(__name__,)

app.secret_key = 'your_secret_key'


def get_userr(token):
  url = DOMAIN + '/api/user?oauth_token={}&client_id={}&client_secret={}'.format(token, CLIENT_ID, CLIENT_SECRET)
  response = requests.get(url)
  data = response.json()
  return data


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/create_session')
def create_session():
  if 'user' in session:
    return redirect(url_for('my_account'))
  else:
    return render_template('redirect.html', client_id=CLIENT_ID, scope='identify+email')


@app.route('/authorized', methods=['POST', 'GET'])
def authorized():
  oauth_token = request.args.get('oauth_token')
  session['token'] = oauth_token
  user = get_userr(session['token'])
  session['user'] = user
  return redirect(url_for('my_account'))


@app.route('/my_account')
def my_account():
  if 'user' in session:
    return render_template('user.html')
  else:
    return redirect(url_for('create_session'))


@app.route('/logout')
def logout():
  if 'user' in session:
    session.pop('user', None)
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run()
```
