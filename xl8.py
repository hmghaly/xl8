from flask import Flask, redirect, url_for, request,render_template, send_file, send_from_directory
from flask import jsonify
import os, sys, json, time, re, copy

app = Flask(__name__)

#app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/assets/<path:path>')
def serve_file(path):
    return send_from_directory('assets', path)  


@app.route('/')
def home_page():
  out_dict={}
  out_dict["message"]="success"
  return json.dumps(out_dict)

  #index_file_dom=DOM(read_file("index.html"))
  #home_repl_dict={".page":""}


if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  serve(app, host="0.0.0.0", port=4000)
  #app.run()
