import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../template')
app = Flask(__name__, tmpl_dir)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return 'It works!'


@app.route('/ws-test')
def ws_test():
    return render_template('websocket_test.html')


@socketio.on('my event', namespace='/ws')
def test_message(message):
    print message
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event', namespace='/ws')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/ws')
def test_connect():
    print "connected"
    emit('my response', {'data': '[Server] You are connected!'})


@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
