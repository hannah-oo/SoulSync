from flask import Flask, render_template, request, abort, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/user-profile')
def user_profile():
    return render_template('user-profile.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=True)
