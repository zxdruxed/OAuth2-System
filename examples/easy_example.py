from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests

CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
DOMAIN = 'http://oauth2system.sytes.net'

app = Flask(__name__)

app.secret_key = 'my_secret_key'


@app.route('/create_session')
def create_session():
  if 'user' in session:
    return redirect(url_for('my_account'))
  else:
    return redirect('{}/oauth2/authorize?client_id={}&scope={}'.format(DOMAIN, CLIENT_ID, 'identify+email'))


@app.route('/authorized', methods=['GET'])
def authorized():
  oauth_token = request.args.get('oauth_token')
  session['token'] = oauth_token

@app.route('/logout')
def logout():
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
