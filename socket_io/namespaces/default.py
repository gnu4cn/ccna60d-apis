#! /usr/bin/python
from flask_socketio import Namespace, emit

class metaNamespace(Namespace):
    def on_connect(self):
        emit('connected', {'data': 'test data'})
        print('已连接')

    def on_disconnect(self):
        emit('disconnected', {'data': 'test data'});
        print('连接断开')

    def on_some_event(self, data):
        emit('some_response', data)
