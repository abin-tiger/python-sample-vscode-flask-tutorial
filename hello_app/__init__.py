from flask import Flask  # Import the Flask class
from aws_xray_sdk.core import patch_all

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_recorder.configure(service='Python Sample Flask application' ,daemon_address="localhost:2000")
XRayMiddleware(app, xray_recorder)

patch_all()