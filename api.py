#! .venv/bin/python
from flask import Flask
from flask_restful import Api

from user.account import (TodoList, Todo, DB_Para)

app = Flask(__name__)

# https://segmentfault.com/q/1010000009235017/a-1020000009241094
# 解决Unicode 字面值问题
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

api = Api(app)


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(DB_Para, '/db_para')

if __name__ == '__main__':
    app.run(debug=True)
