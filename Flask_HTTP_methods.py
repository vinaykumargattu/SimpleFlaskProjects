from flask import Flask

app = Flask(__name__)
@app.route('/')
def simple():
    return "This is simple"
@app.route('/post',methods=['POST'])
def post_method():
    return "This is POST method"

@app.route('/get', methods=['GET'])
def get_method():
    return "This is GET method"

if __name__=='__main__':
    app.run(debug=True)