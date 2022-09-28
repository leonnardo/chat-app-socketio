import socketio
import sys

client = socketio.Client()
client.connect('http://localhost:5000')

@client.on('message')
def message_handler(message):
    if message['user'] != client.sid:
        print(f'message received: {message}')


while True:
    message = sys.stdin.readline()
    client.emit('message', {'user': client.sid, 'text': message})

