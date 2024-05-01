#/usr/bin/python3
"""
This module contains endpoint(route) status
"""

Create flask app; app_views

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns a JSON response with the status "OK".

    Returns:
        Response: A JSON response with the status "OK".
    """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    Retrieves the number of each object by type.
    """
    stats = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User)
    }
    return jsonify(stats)
