from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from time import sleep
from signal import signal, SIGINT

ADDRESS = '0.0.0.0'
PORT = 5000

app = Flask(__name__)
app.secret_key = 'secret'
sio = SocketIO(app)

running = True


def quit_handler(_, __):
    global running
    running = False
    quit()


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':

    signal(SIGINT, quit_handler)

    sio.run(app, host=ADDRESS, port=PORT, debug=True)
