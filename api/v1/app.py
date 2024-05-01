#!/usr/bin/python3

"""
This module contains the principal application
"""

from os import getenv
from Flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == "__main__":
 HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)

@app.teardown_appcontext
def close_db(exception):
    """
    Close the storage when the application context ends.

    Args:
        exception (Exception): An optional exception
        that occurred during request handling.
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    response = make_response(jsonify(error="Not found"), 404)
    return response

