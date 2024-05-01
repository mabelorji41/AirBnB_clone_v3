#!/usr/bin/python3

Create flask app blueprint

from flask import blueprint

app_views = blueprint('app_views', __name__, api_prefix='/api/v1')

from api.v1.views.index import "

