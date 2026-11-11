import logging
import traceback
#logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)

import os, sys, json, time, re, copy, base64
import requests
from itertools import groupby
import pandas as pd


from flask import Flask, redirect, url_for, request,render_template, send_file, send_from_directory
#from werkzeug.middleware.proxy_fix import ProxyFix
from flask import jsonify

#app = Flask(__name__)

#app.wsgi_app = ProxyFix(app.wsgi_app)
app = Flask(__name__)

# # Trust exactly one proxy: Apache on localhost
# app.wsgi_app = ProxyFix(
#     app.wsgi_app,
#     x_for=1,
#     x_proto=1,
#     x_host=1
# )

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1
)


@app.route("/client-ip")
def client_ip():
    return {"ip": request.remote_addr}  


@app.route("/debug-ip")
def debug_ip():
    return {
        "remote_addr": request.remote_addr,
        "x_forwarded_for": request.headers.get("X-Forwarded-For"),
        "x_real_ip": request.headers.get("X-Real-IP"),
        "access_route": request.access_route
    }


@app.route("/debug-headers")
def debug_headers():
    return {
        "all_headers": dict(request.headers),
        "remote_addr": request.remote_addr,
        "environ_x_forwarded_for": request.environ.get("HTTP_X_FORWARDED_FOR")
    }


@app.route('/assets/<path:path>')
def serve_file(path):
    return send_from_directory('assets', path)  


@app.errorhandler(Exception)
def exception_handler(error):
  out={}
  #out["repr"]=repr(error)
  #out["test"]=dir(error)
  try: out["error_code"]=error.code #dir(error)
  except: pass
  #out["error_description"]=error.description
  
  ex=Exception
  out["error_string"]=str(ex)
  out["trace"]=traceback.format_exc()
  #append_line(json.dumps(out),error_fpath)
  
  return json.dumps(out)


@app.route('/')
def home_page():
  out_dict={}
  out_dict["message"]="success"
  with open("index.html") as fopen: content0=fopen.read()
  #return json.dumps(out_dict)

  #index_file_dom=DOM(read_file("index.html"))
  #home_repl_dict={".page":""}
  return content0

  #return read_file("index.html") #json.dumps(out_dict)



if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  #serve(app, host="0.0.0.0", port=4000)

serve(
    app,
    host="0.0.0.0",
    port=4000,
    trusted_proxy="127.0.0.1",
    trusted_proxy_headers={
        "x-forwarded-for",
        "x-forwarded-proto",
        "x-forwarded-host"
    }
)

  #app.run()

# from flask import Flask, request
# from werkzeug.middleware.proxy_fix import ProxyFix

# app = Flask(__name__)

# # Trust exactly one proxy: Apache on localhost
# app.wsgi_app = ProxyFix(
#     app.wsgi_app,
#     x_for=1,
#     x_proto=1,
#     x_host=1
# )

# @app.route("/client-ip")
# def client_ip():
#     return {"ip": request.remote_addr}  