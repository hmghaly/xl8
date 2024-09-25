from flask import Flask, redirect, url_for, request,render_template, send_file, send_from_directory
from flask import jsonify

if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  serve(app, host="0.0.0.0", port=4000)
  #app.run()
