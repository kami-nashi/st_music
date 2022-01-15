from flask import Flask, render_template, request
import lib.logicMain as music
import json
import st_dbConf

app = Flask(__name__)
appConfig = st_dbConf.baseConfig()
app.config['SECRET_KEY'] = appConfig

@app.route('/', methods=['GET'])
def home():
    title = "This is a test"
    name = "Ashley"
    return render_template('index.html', title=title, name=name)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    music.musicDownload(projectpath)
    return render_template('index.html', title="title", name=projectpath)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022, use_reloader=True, debug=True)
