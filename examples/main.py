from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests

CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
DOMAIN = 'emeraldermine.onpella.app'

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


if __name__ == '__main__':
  app.run()
