from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests

app = Flask(__name__)

OAUTH2_CLIENT_ID = YOUR_CLIENT_ID
OAUTH2_CLIENT_SECRET = YOUR_CLIENT_SECRET

OAUTH2_BASE_URL = 'http://oauth2system.sytes.net'
OAUTH2_AUTHRORIZATION_URL = OAUTH2_BASE_URL + '/oauth2/authorize'
OAUTH2_API_BASE_URL = OAUTH2_BASE_URL + '/api'

app.secret_key = 'my_secret_key'


@app.route('/login')
def login():
  if 'token' not in session:
    scope = 'identify+email'
    return redirect(OAUTH2_AUTHRORIZATION_URL + '?client_id=' + str(OAUTH2_CLIENT_ID) + '&scope=' + scope)
  else:
    return render_template('login.html')


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


def get_user(token):
  url = DOMAIN + '/api/user?oauth_token={}&client_id={}&client_secret={}'.format(token, CLIENT_ID, CLIENT_SECRET)
  response = requests.get(url)
  data = response.json()
  return data


@app.route('/my_account')
def my_account():
  if 'token' in session:
    user = get_user(session['token']
    return user


if __name__ == '__main__':
  app.run()
