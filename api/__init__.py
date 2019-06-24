import os
from flask import Flask, send_from_directory

app = Flask(__name__)
app.config['PWA_ASSETS'] = os.path.join(os.getcwd(), 'pwa', 'dist')


################### RETURNS LATEST BUILD OF PWA ##############################
@app.route("/")
def index_pwa_html():
    return send_from_directory(app.config['PWA_ASSETS'], 'index.html', as_attachment=False)

@app.route("/<path:filename>")
def pwa_assets_request(filename):
    print('FILE::', filename)
    return send_from_directory(app.config['PWA_ASSETS'], filename, as_attachment=False)

##############################################################################

from api.routes import *