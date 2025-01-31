from flask import Flask, render_template,request,jsonify
import pymysql
import time

app = Flask(__name__)

text=[]

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_api',methods=['POST'])
def login_api():
    username=request.form.get('username')
    password=request.form.get('password')
    info = {
        "errno": 0,
        "msg": "ok"
    }
    conn = pymysql.connect(host='localhost',user='root',password='canyang0207+',database='web')
    cursor = conn.cursor()
    sql = "select password from users where username='%s'"%username
    cursor.execute(sql)
    rows=cursor.fetchall()
    passs=rows[0][0]
    if  password==passs:
        pass
    else:
        info['errno'] = 1
        info['msg'] = "wrong"
    cursor.close()
    conn.close()
    return info

@app.route('/list')
def blog_list():
    return render_template('list.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/upload',methods=["POST"])
def upload():
    history=request.form.get('notes')
    title=request.form.get('titles')
    conn = pymysql.connect(host='localhost',user='root',password='canyang0207+',database='web')
    cursor = conn.cursor()
    sql = "insert into notes(contents,create_time,title) values(%s,%s,%s)"
    cursor.execute(sql,(history,int(time.time()),title))
    conn.commit()
    cursor.execute(sql)
    rows=cursor.fetchall()

    return jsonify(text)



if __name__== '__main__':
    app.run(debug=True)