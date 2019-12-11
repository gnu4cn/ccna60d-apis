#! /usr/bin/python
from socket_io.namespaces.default import defaultNamespace

def generate_sockets(socketio):

    socketio.on_namespace(defaultNamespace('/news'))


