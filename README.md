# Oauth2System

### OAuth2System - a simple authorization system for multiple sites or projects.

## How do I create my own app?

#### [Here](https://emeraldermine.onpella.app/apps) you can create your own application.

## How can I create authorization using my application?

### To do this, you will need the CLIENT ID you previously received

## A Simple Example ([Python](https://www.python.org) - [Flask](https://github.com/pallets/flask). )

### Importing the necessary libraries

```python
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests
```

### Adding variables

```python
CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET

app.secret_key = 'my_secret_key'
```

### Adding an OAuth2 page

## Under the scope value, you must put the values that the system will receive

## Identify - access to the displayed and user name, ID and avatar of the user.

## Email - access to the user's email

## If you want to specify multiple values at once, then the scope value should be something like "identify+email". (SPECIFY THE VALUES IN SMALL LETTERS!)

```python
@app.route('/create_session')
def create_session():
  if 'user' in session:
    return redirect(url_for('my_account'))
  else:
    return render_template('redirect.html')
```
