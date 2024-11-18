import logging
import traceback
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)

import os, sys, json, time, re, copy, base64
import requests
from itertools import groupby
import pandas as pd
from flask import Flask, redirect, url_for, request,render_template, send_file, send_from_directory
from flask import jsonify

from code_utils.general import *
from code_utils.web_lib import *
from code_utils.backend_utils import *
from code_utils.pandas_utils import *
from code_utils.align_utils import *
from code_utils.arabic_lib import *
from code_utils.classification_utils import *


app = Flask(__name__)

#app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/assets/<path:path>')
def serve_file(path):
    return send_from_directory('assets', path)  


@app.route('/')
def home_page():
  out_dict={}
  out_dict["message"]="success"
  #return json.dumps(out_dict)

  #index_file_dom=DOM(read_file("index.html"))
  #home_repl_dict={".page":""}

  return read_file("index.html") #json.dumps(out_dict)


@app.route('/align_api')
def align_api():
  out_dict={}
  out_dict["message"]="success"
  return json.dumps(out_dict)



if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  serve(app, host="0.0.0.0", port=4000)
  #app.run()
