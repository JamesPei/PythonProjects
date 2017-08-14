from gevent import monkey; monkey.patch_all()
from flask import Flask, render_template, request, json

from gevent import queue
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
app.debug = True


class Room(object):

    def __init__(self):
        self.users = set()
        self.messages = []

    def backlog(self, size=25):
        return self.messages[-size:]

    def subscribe(self, user):
        self.users.add(user)

    def add(self, message):
        for user in self.users:
            print user
            user.queue.put_nowait(message)
        self.messages.append(message)


class User(object):
    def __init__(self):
        self.queue = queue.Queue()

rooms = {'python': Room(), 'django': Room(), }

users = {}


@app.route('/')
def choose_name():
    return render_template('choose.html')


@app.route('/<room>/<uid>')
def join(room, uid):
    user = users.get(uid, None)

    if not user:
        users[uid] = user = User()

    activate_room = rooms[room]
    activate_room.subscribe(user)
    print 'subscribe', activate_room, user

    message = activate_room.backlog()

    return render_template('room.html', room=room, uid=uid, message=message)


@app.route("/put/<room>/<uid>", methods=["POST"])
def poll(uid):
    try:
        msg = users[uid].queue.get(timeout=10)
    except queue.Empty:
        msg = []
    return json.dumps(msg)


if __name__ == '__main__':
    http = WSGIServer(('', 5000), app)
    http.serve_forever()