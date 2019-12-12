#! /usr/bin/python
from socket_io.namespaces.default import metaNamespace

newsNamespace = metaNamespace('/news')

def generate_sockets(socketio):

    socketio.on_namespace(newsNamespace)


