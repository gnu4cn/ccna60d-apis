#! /usr/bin/python
from socket_io.namespaces.default import metaNamespace

def generate_sockets(socketio):

    socketio.on_namespace(metaNamespace('/news'))


