#!/usr/bin/env python3
from storage.storage_units import *
from items.item import *
import sys , os 

import pkg_resources



import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "Nadav Salman")
    return "{} CI-CD template . (Deployed uding : GCP Cloud Run) !!! \n".format(name)

@app.route("/storage")
def get_storage():
	return say_kuku()

@app.route("/item")
def get_item():
	return " {}! \n".format(secrate_massage())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))