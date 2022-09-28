from flask import Flask
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)


@socketio.on('message')
def message_handler(message):
    send(message, broadcast=True)
