from http import HTTPStatus

from flask import Flask, jsonify, request, make_response


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}

        @app.route('/user', methods=['POST'])
        def create_user():
            data = request.get_json()
            if 'name' not in request.get_json() or not request.get_json()['name']:
                return jsonify({'errors': {'name': 'This field is required'}}), HTTPStatus.UNPROCESSABLE_ENTITY
            else:
                name = data.get("name")
                users[name] = {}
                return jsonify({"data": f"User {name} is created!"}), HTTPStatus.CREATED

        @app.route('/user/<name>', methods=['GET'])
        def get_user(name: str):
            if name in users:
                return jsonify({"data": f"My name is {name}"}), HTTPStatus.OK
            return make_response(jsonify(), HTTPStatus.NOT_FOUND)

        @app.route('/user/<name>', methods=['PATCH'])
        def update_user(name: str):
            data = request.get_json()
            new_name = data.get("name")
            if new_name is None:
                return make_response(jsonify(), HTTPStatus.NOT_FOUND)
            del users[name]
            users[new_name] = {}
            return jsonify({"data": f"My name is {new_name}"}), HTTPStatus.OK

        @app.route('/user/<name>', methods=['DELETE'])
        def delete_user(name):
            print(users)
            if name in users:
                del users[name]
                response = "", HTTPStatus.NO_CONTENT
            else:
                response = "", HTTPStatus.NOT_FOUND
            return response
