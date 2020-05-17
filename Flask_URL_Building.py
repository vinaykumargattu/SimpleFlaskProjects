from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin/<admin>')
def admin(admin):
    print("this is admin")
    return "This is admin %s"%admin

@app.route('/user/<user>')
def user(user):
    print("This is user")
    return "This is user%s"%user

@app.route('/guest/<guest>')
def guest(guest):
    if guest=="vinay":
         return redirect(url_for('admin', admin=guest))
    else:
        return redirect(url_for('user', user=guest))

if __name__=='__main__':
    app.run(debug=True)
