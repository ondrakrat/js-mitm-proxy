from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return 'It works!'


@app.route('/ws-test')
def ws_test():
    return render_template('websocket_test.html')


@app.route('/form')
def form():
    return render_template('form.html')


@socketio.on('my event', namespace='/ws')
def test_message(message):
    print message
    emit('my response', {'data': '[Server] Event received'})


@socketio.on('keypress', namespace='/ws')
def test_message(message):
    print message
    emit('my response', {'data': '[Server] Key accepted'})


@socketio.on('connect', namespace='/ws')
def test_connect():
    print "connected"
    emit('my response', {'data': '[Server] You are connected!'})


@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
