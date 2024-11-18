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


@app.route('/align_api', methods = ['POST',"GET"])
def align_api():
  out_dict={}
  out_dict["message"]="success"
  if request.method == 'POST':
      posted_data=request.data.decode("utf-8")
      posted_data_dict=json.loads(posted_data)   
      out_dict["data"]=posted_data_dict
      src_text_input=posted_data_dict.get("src_text_input","")
      trg_text_input=posted_data_dict.get("trg_text_input","")
      if src_text_input and trg_text_input: out_dict["align_output"]=content_align(src_text_input,trg_text_input)

  return json.dumps(out_dict)


#Sentence Alignment Code
def trg_tokenize(txt):
  txt=clean_ar(txt)
  return general.tok_uc(txt)

align_params0={}
align_params0["default_len_ratio"]=0.85
align_params0["src_tok_function"]=general.tok_uc
align_params0["trg_tok_function"]=trg_tokenize


def content_align(src_content,trg_content,align_params=align_params0):
  src_sents=ssplit(src_content)
  trg_sents=ssplit(trg_content)
  s_align=sent_align(source, target,align_params)
  out_dict={"src":src_sents,"trg":trg_sents,"alignment":s_align.aligned_pairs}
  return out_dict







if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  serve(app, host="0.0.0.0", port=4000)
  #app.run()
