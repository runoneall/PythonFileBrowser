import flask
import Config

app = flask.Flask(__name__)

@app.route('/file-online/<path:filepath>')
def FileOnlineManager(filepath):
    pass

@app.route('/file-api/<path:action>')
def FileApiManager(action):
    pass

@app.route('/login')
def LoginManager():
    pass

@app.route('/sysconfig/<path:action>')
def SysConfigManager(action):
    pass