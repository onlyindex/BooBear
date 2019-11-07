from flask import Flask,render_template
from datetime import timedelta

app = Flask(__name__, static_folder='', static_url_path='', instance_relative_config=True)
#
# 设置为开发模式
app.config['DEBUG'] = True

# 设置缓存时间1s
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)



# 设置假装数据
user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


# 基础模板测试仪
@app.route('/base2')
def base():
    return render_template('base2_1.html')

# 首页

@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/home2')
def home2():
    return render_template('home2_1.html')

@app.route('/home3')
def home3():
    return render_template('base3.html')

# 绘本馆
# 所有书按照分类排列  lib/book/1
# @app.route('/lib')
# def lib():
#     return render_template('booktype.html')


@app.route('/lib2')
def lib2():
    return render_template('booktype2.html')

# 绘本馆
# 某本书 lib/book/1
@app.route('/lib/book/1')
def lib3():
    return render_template('lib.html')

# 某本书所有笔记  lib/book/1/note


# 用户所有书单  u/1/booklist


# 用户某个书单   u/1/booklist/2333
@app.route('/booklist')
def booklist():
    return render_template('booklist.html')

@app.route('/booklist2')
def booklist2():
    return render_template('booklist2.html')

# 用户 u/4
@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/user2')
def user2():
    return render_template('user2.html')


@app.route('/user3')
def user3():
    return render_template('user3.html')
# 用户主页？


# 用户的书架  /u/1/shelf/  wanna_read read_ing  mark_read
@app.route('/shelf')
def shelf():
    return render_template('shelf.html')
# 用户发布读书笔记 /u/1/note/ article/images/video/play ？？？？

# 用户听书历史
@app.route('/record')
def record():
    return render_template('record.html')







# 用户所有看的电影
@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)
