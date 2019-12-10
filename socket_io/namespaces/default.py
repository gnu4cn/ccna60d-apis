#! /usr/bin/python
from flask_socketio import Namespace, emit

class defaultNamespace(Namespace):
    def on_connect(self):
        emit('connected')
        print('Test')

    def on_disconnect(self):
        emit('disconnected')
        pass

    def on_some_event(self, data):
        emit('some_response', data)
