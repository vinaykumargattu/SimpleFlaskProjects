from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return "This is home"

@app.route('/about')
def about():
    return "This is about"

if __name__=='__main__':
    app.run(debug=True)