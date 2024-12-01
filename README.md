# Oauth2System

## OAuth2System - a simple authorization system for multiple sites or projects.

## How do I create my own app?

### [Here](http://oauth2system.sytes.net/apps) you can create your own application.

## How can I create authorization using my application?

### To do this, you will need the CLIENT ID you previously received

## A Simple Example ([Python](https://www.python.org) - [Flask](https://github.com/pallets/flask). )

## Importing the necessary libraries

```python
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests

app = Flask(__name__)

#

if __name__ == '__main__':
  app.run()
```

### Adding variables

```python

OAUTH2_CLIENT_ID = YOUR_CLIENT_ID
OAUTH2_CLIENT_SECRET = YOUR_CLIENT_SECRET

OAUTH2_BASE_URL = 'http://oauth2system.sytes.net'
OAUTH2_AUTHRORIZATION_URL = OAUTH2_BASE_URL + '/oauth2/authorize'
OAUTH2_API_BASE_URL = OAUTH2_BASE_URL + '/api'

app.secret_key = 'my_secret_key'
```

## Adding an OAuth2 page

### Under the scope value, you must put the values that the system will receive

### Identify - access to the displayed and user name, ID and avatar of the user.

### Email - access to the user's email

### If you want to specify multiple values at once, then the scope value should be something like "identify+email". (SPECIFY THE VALUES IN SMALL LETTERS!)

```python
@app.route('/login')
def login():
  if 'token' not in session:
    scope = 'identify+email'
    return redirect(OAUTH2_AUTHRORIZATION_URL + '?client_id=' + str(OAUTH2_CLIENT_ID) + '&scope=' + scope)
  else:
    return render_template('login.html')
```

## Redirect Uri

### The redirect uri of the application that you previously specified is a site page that accepts an OAuth2 token (it will be useful for us to work with the API).

#### The redirect uri of your application must contain a link that will receive an authorization token. In our case, this is "/confirm_login".

```python
@app.route('/confirm_login', methods=['GET'])
def confirm_login():
  oauth_token = request.args.get('oauth_token')
  session['token'] = oauth_token

  user = get_user(oauth_token)
  if users.find_one({'id': user['id']}) == None:
    users.insert_one({'id': user['id'], 'token': oauth_token})

  return redirect(url_for('index'))


@app.route('/logout')
def logout():
  if 'token' in session:
    session.pop('token', None) 
  return redirect(url_for('index'))
```

# Working with the API

### In order to get a user, we will need a previously obtained OAuth2 token, as well as the CLIENT ID and CLIENT SECRET of your application.

```python
def get_user(token):
  url = OAUTH2_API_BASE_URL + '/user?oauth_token={}&client_id={}&client_secret={}'.format(token, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)
  response = requests.get(url)
  data = response.json()
  return data
```

```python
@app.route('/my_account')
def my_account():
  if 'token' in session:
    user = get_user(session['token']
    return user
```
