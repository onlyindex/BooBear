from flask import Flask,render_template
from datetime import timedelta

app = Flask(__name__)

# 设置缓存时间1s
app.config['SEND_FILE_MAX_AGE_DEFAULT '] = timedelta(seconds=1)

@app.route('/')
def hello_world():
    return render_template('home.html')

