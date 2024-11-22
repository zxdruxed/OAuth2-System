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
