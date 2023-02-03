from jaeger_client import Config
from os import getenv


JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')
WEBSERVER_HOST = getenv('WEBSERVER_HOST', 'localhost')

config = Config(config={'sampler': {'type': 'const', 'param': 1},
                        'logging': True,
                        'local_agent': {'reporting_host': JAEGER_HOST}},
                service_name="jaeger_opentracing_example")
tracer = config.initialize_tracer()


import opentracing
from flask_opentracing import FlaskTracing

from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use

opentracing_tracer = tracer
tracing = FlaskTracing(opentracing_tracer, True, app)
