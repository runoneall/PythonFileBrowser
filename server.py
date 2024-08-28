import flask
import Config

app = flask.Flask(__name__)

@app.route('/')
def IndexPage():
    return flask.render_template('index.html')

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

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8501',
        debug=True
    )