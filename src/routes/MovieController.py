from flask import Blueprint, jsonify
from pip import main

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    return jsonify({'message': 'anapatino'})
