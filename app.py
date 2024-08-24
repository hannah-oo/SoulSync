from flask import Flask, render_template, request, abort, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('main.html')

if __name__ == '__main__':
    socketio.run(app)