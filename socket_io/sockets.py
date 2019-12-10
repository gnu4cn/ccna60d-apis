#! /usr/bin/python
from flask_socketio import SocketIO
from socket_io.namespaces.news import NewsNamespace

def generate_sockets(app):

    socketio = SocketIO()

    socketio.init_app(app)

    socketio.on_namespace(NewsNamespace('/news'))

    socketio.run(app, cors_allowed_origins='*', debug=True)

