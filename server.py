import flask
import MakeFileList

app = flask.Flask(__name__)

@app.route('/')
def IndexPage():
    return flask.render_template('index.html')

@app.route('/file-online/<int:id_>')
@app.route('/file-online/<int:id_>/<path:path_>')
def FileOnlineManager(*args, **kwargs):
    FileList = list()
    if 'path_' in kwargs:
        FileList = MakeFileList.GetList(kwargs['id_'], kwargs['path_'])
    if 'path_' not in kwargs:
        FileList = MakeFileList.GetRootList(kwargs['id_'])
    print(FileList)

@app.route('/file-action')
def FileAction():
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