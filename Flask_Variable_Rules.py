from flask import Flask, request

app = Flask(__name__)

@app.route('/sname/<name>', methods = ['POST'])
def myapp(name):
    print("my name is ", name)
    return "my name is %s" % name

@app.route('/sid/<int:sid>', methods=['POST'])
def sid(sid):
    #sid=request.form['sid']
    print("my id is ", sid)
    return "my id is %d"%sid
if __name__=='__main__':
    app.run(debug=True)
