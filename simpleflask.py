from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Om Nmahashivaya Love you sujju "

if __name__ == '__main__':
    app.run(debug=True)

