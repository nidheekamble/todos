from api import app

if __name__ == '__main__':
  print('SERVING PWA FILES FROM:' + app.config['PWA_ASSETS'])
  app.run(host='0.0.0.0', port=5000, debug=True)