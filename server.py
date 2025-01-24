from flask import Flask, render_template,request,jsonify

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
    if username=='licanyang' and password=='qqqqqqqq':
        pass
    else:
        info['errno'] = 1
        info['msg'] = "wrong"
    
    return info


if __name__== '__main__':
    app.run(debug=True)