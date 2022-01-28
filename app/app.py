from flask import Flask, render_template, request, send_file
import lib.logicMain as music
import lib.mqSendMessage as sendMusic
import json
import st_dbConf




app = Flask(__name__)
appConfig = st_dbConf.baseConfig()
app.config['SECRET_KEY'] = appConfig
app.config["SKATER_MUSIC"] = "/tmp"

@app.route('/', methods=['GET'])
def home():
    title = "This is a test"
    name = "Ashley"
    return render_template('index.html', title=title, name=name)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    #print(projectpath)
    #music.musicDownload(projectpath)
    sendMusic.mqsend_downloader(projectpath)
    return render_template('index.html', title="title", name=projectpath)

@app.route('/download')
def download_file():
    file = 'creating.mp3'
    return send_file("/tmp/"+ file, as_attachment=True, max_age=0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022, use_reloader=True, debug=True)
