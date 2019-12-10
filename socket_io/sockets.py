#! /usr/bin/python
from flask_socketio import SocketIO
from socket_io.namespaces.default import defaultNamespace

def generate_sockets(app):

    socketio = SocketIO(app, cors_credentials=False)

    socketio.on_namespace(defaultNamespace('/'))
    socketio.on_namespace(defaultNamespace('/news'))

    socketio.run(debug=True)

