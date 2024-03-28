from flask import Flask, make_response, jsonify, request, session
from flask_restful import Api, Resource
from models import db, User
from flask_cors import CORS
from flask_migrate import Migrate
from config import ApplicationConfig


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
api = Api(app=app)
CORS(app=app)

migrate = Migrate(app=app, db=db)
db.init_app(app=app)

class Index(Resource):
    def get(self):
        response = make_response(jsonify("Welcome"), 200)
        return response
api.add_resource(Index, '/', endpoint="index")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]

        response = make_response(
            jsonify(users),
            200
        )

        return response
    
api.add_resource(Users, '/users', endpoint="users")

class SignUp(Resource):
    def post(self):
        username = request.get_json()["username"]
        password = request.get_json()["password"]

        if username:
            user = User(
                username = username,
            )

            user.password_hash = password

            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id

            response = make_response(
                jsonify(user.to_dict()), 201
            )

            return response
        response = make_response(
            jsonify({"error": "username or email exists"}), 401
        )
        return response
    
api.add_resource(SignUp, '/signup', endpoint='signup')


if __name__ == "__main__":
    app.run(port=5555, debug=True)