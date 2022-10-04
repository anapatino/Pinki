from flask import Flask
from config import config

# Routes
from routes import MovieController

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not found Page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BluePrints
    app.register_blueprint(MovieController.main, url_prefix='/api/movies')

    # Error Handlers
    app.register_error_handler(404, page_not_found)
    app.run()
