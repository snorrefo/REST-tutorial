from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]

    @app.route('/')
    def index():
        return "Hello, World!"

    # curl -i http://localhost:5000/todo/api/v1.0/tasks
    @app.route('/todo/api/v1.0/tasks', methods=['GET'])
    def get_tasks():
        return jsonify({'tasks': tasks})

    # curl -i http://localhost:5000/todo/api/v1.0/tasks/3
    @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)
        return jsonify({'task': task[0]})

    # curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://192.168.99.100:5000/todo/api/v1.0/tasks
    @app.route('/todo/api/v1.0/tasks', methods=['POST'])
    def create_task():
        if not request.json or 'title' not in request.json:
            abort(400)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201

    # curl -i -H "Content-Type: application/json" -X PUT -d '{"title":true}' http://192.168.99.100:5000/todo/api/v1.0/tasks/2
    @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'title' in request.json and type(request.json['title']) != str:
            abort(400)
        if ('description' in request.json and
                type(request.json['description']) is not str):
            abort(400)
        if 'done' in request.json and type(request.json['done']) is not bool:
            abort(400)
        task[0]['title'] = request.json.get('title', task[0]['title'])
        task[0]['description'] = \
            request.json.get('description', task[0]['description'])
        task[0]['done'] = request.json.get('done', task[0]['done'])
        return jsonify({'task': task[0]})

    @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return jsonify({'result': True})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': '404 Not found'}), 404)

    return app
