from flask import Flask
from flask_restful import Api
import json
import sys

# get config file
try:
    with open("config_file.json") as configuration:
        config_file = json.load(configuration)
        API_VERSION = config_file["API_VERSION"]
except FileNotFoundError as e:
    sys.exit(1)


app = Flask(config_file["APP_NAME"])
api = Api(app)

# --------------
#       API
# --------------
from resources.index import Index
from resources.todos import TodoList, Todo

api.add_resource(Index, "/api/{}/".format(API_VERSION))
api.add_resource(TodoList, "/api/{}/todos/".format(API_VERSION))
api.add_resource(Todo, "/api/{}/todos/<todo_id>".format(API_VERSION))


if __name__ == "__main__":
    app.run()
