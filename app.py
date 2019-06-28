# import the necessary packages
import decimal
from flask import Flask
from flask import request
from tempfile import mkdtemp
from werkzeug import serving
import os
import requests
import ssl
from werkzeug.utils import secure_filename
from flask import jsonify
import random
import string
import json
from uuid import uuid4
import sys
import random

from flask import send_file
import subprocess
import traceback

try:  # Python 3.5+
    from http import HTTPStatus
except ImportError:
    try:  # Python 3
        from http import client as HTTPStatus
    except ImportError:  # Python 2
        import httplib as HTTPStatus


app = Flask(__name__)


# define a predict function as an endpoint 
@app.route("/detect", methods=["POST"])
def detect():

    try:
        text = request.json["text"]

        cli_str = "franc \"" + text + "\""
    
        result = subprocess.run(['franc', text], stdout=subprocess.PIPE)

        results = []
        results.append({"language": result.stdout.decode('ascii').strip()})

        return json.dumps(results), 200

    except:
        traceback.print_exc()
        return {'message': 'input error'}, 400



if __name__ == '__main__':

    port = 5000
    
    host = '0.0.0.0'

    app.run(host=host, port=port, threaded=True)

