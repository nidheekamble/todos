from api import app
import time
#Sample AJAX REQUEST

@app.route('/api/hello', methods=['POST'])
def hello():
  time.sleep(1)
  return 'Hello'