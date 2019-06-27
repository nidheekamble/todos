from flask import request
from api import app
import time
#Sample AJAX REQUEST

@app.route('/api/hello', methods=['POST'])
def hello():
  time.sleep(1)
  return 'Hello'

@app.route('/api/login', methods=['POST'])
def login():
  
  try:
    username = request.form['username']
    pwd      = request.form['password']

    if username == 'foo' and pwd == 'bar':
      return ('', 200)
  except Exception as e:
    return('', 400)

  return ('', 401)