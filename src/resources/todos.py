from flask_restful import reqparse, abort, Resource


parser = reqparse.RequestParser()
parser.add_argument("task")


# MOCKED DATA
TODOS = {
    "1": {
        "task": "Hacer la compra"
    },
    "2": {
        "task": "Comprar cosas"
    },
    "3": {
        "task": "Preparar maleta para el viaje"
    }
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
