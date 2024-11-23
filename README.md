# Oauth2System

## OAuth2System - a simple authorization system for multiple sites or projects.

## How do I create my own app?

### [Here](https://emeraldermine.onpella.app/apps) you can create your own application.

## How can I create authorization using my application?

### To do this, you will need the CLIENT ID you previously received

## A Simple Example ([Python](https://www.python.org) - [Flask](https://github.com/pallets/flask). )

## Importing the necessary libraries

```python
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests

#

if __name__ == '__main__':
  app.run()
```

### Adding variables

```python
CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
DOMAIN = 'emeraldermine.onpella.app'

app.secret_key = 'my_secret_key'
```

## Adding an OAuth2 page

### Under the scope value, you must put the values that the system will receive

### Identify - access to the displayed and user name, ID and avatar of the user.

### Email - access to the user's email

### If you want to specify multiple values at once, then the scope value should be something like "identify+email". (SPECIFY THE VALUES IN SMALL LETTERS!)

```python
@app.route('/create_session')
def create_session():
  if 'user' in session:
    return redirect(url_for('my_account'))
  else:
    return redirect('{}/oauth2/authorize?client_id={}&scope={}'.format(DOMAIN, CLIENT_ID, 'identify+email'))
```

## Redirect Uri

### The redirect uri of the application that you previously specified is a site page that accepts an OAuth2 token (it will be useful for us to work with the API).

```python
@app.route('/authorized', methods=['GET'])
def authorized():
  oauth_token = request.args.get('oauth_token')
  session['token'] = oauth_token

@app.route('/logout')
def logout():
  session.pop('token', None)
  return redirect(url_for('index'))
```

# Working with the API

### In order to get a user, we will need a previously obtained OAuth2 token, as well as the CLIENT ID and CLIENT SECRET of your application.

```python
def get_user(token):
  url = DOMAIN + '/api/user?oauth_token={}&client_id={}&client_secret={}'.format(token, CLIENT_ID, CLIENT_SECRET)
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
