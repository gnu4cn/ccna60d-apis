#! /usr/bin/python
from flask_socketio import Namespace, emit

class NewsNamespace(Namespace):
    def on_connect(self):
        print('Test')

    def on_disconnect(self):
        pass

    def on_some_event(self, data):
        emit('some_response', data)
