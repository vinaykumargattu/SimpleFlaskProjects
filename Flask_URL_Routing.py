from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    print("This is Home Functionis")
    return "This is HOME"
@app.route('/about')
def about():
    print("This is ABOUT Function")
    return "This is ABOUT"
@app.route('/contact')
def contact():
    print("This is CONTACT Function")
    return "This is CONTACT"

if __name__=='__main__':
    app.run(debug=True)
