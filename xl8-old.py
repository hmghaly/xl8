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
from code_utils.qa_utils import *

from code_utils.classification_utils import *


app = Flask(__name__)

#app.wsgi_app = ProxyFix(app.wsgi_app)



normative_wb_path="https://docs.google.com/spreadsheets/d/e/2PACX-1vSpf4wpYxSkFFC84xMNFFVM_LKWtQo8wIchL8sksiNSQLZktwPTnLW9jmF2jVpv4gORd9gD9QtcrTGZ/pub?output=xlsx"
normative_wb=get_wb_data_dict(normative_wb_path)

ar_warning_items=normative_wb["arabic_warnings"]
ar_warning_list=[]
for it0 in ar_warning_items:
  word0,note0=it0["word"],it0["note"]
  ar_warning_list.append((note0,word0))

normative_items=normative_wb["normative"]
normative_list=[]
for it0 in normative_items:
  en_item_raw0,ar_item_raw0=it0["en"],it0["ar"]
  normative_list.append((en_item_raw0,ar_item_raw0))

warning_src_inv_dict0,warning_trg_inv_dict0=qa_list_inv(ar_warning_list)
normative_src_inv_dict0,normative_trg_inv_dict0=qa_list_inv(normative_list,include_self=True)

qa_param_list=[]
qa_param_list.append({"src_inv_dict":{},"trg_inv_dict":warning_trg_inv_dict0,"qa_type":"warning"})
qa_param_list.append({"src_inv_dict":normative_src_inv_dict0,"trg_inv_dict":normative_trg_inv_dict0,"qa_type":"matching"})





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
  append_line(json.dumps(out),error_fpath)
  
  return json.dumps(out)


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
      bitext_input=posted_data_dict.get("bitext_input","")
      try:
        if src_text_input and trg_text_input: out_dict["align_output"]=content_align(src_text_input,trg_text_input)
        elif bitext_input: out_dict["align_output"]=bitext_process(bitext_input)
      except Exception as ex:
        out_dict["error_string"]=str(ex)
        out_dict["trace"]=traceback.format_exc()
  

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
  src_sents=ssplit(src_content,add_br=True)
  trg_sents=ssplit(trg_content,add_br=True)
  s_align=sent_align(src_sents, trg_sents,align_params)
  out_dict={"src":src_sents,"trg":trg_sents,"alignment":s_align.aligned_pairs}
  return out_dict


def bitext_process(bitext_str_input):
  bitext_pairs=split_bitext_str(bitext_str_input,exclude_single=True)
  src_sents,trg_sents,aligned_pairs=[],[],[]
  for i0, a0 in enumerate(bitext_pairs):
    src_seg0,trg_seg0=a0
    idx_pair=([i0],[i0])
    src_sents.append(src_seg0)
    trg_sents.append(trg_seg0)
    cur_dict={}
    src_toks0,trg_toks0=tok(src_seg0),tok(trg_seg0)
    cur_qa_matches=qa_get_matching_list_from_params(qa_param_list,src_toks0,trg_toks0)
    prefix0=f'sent{i0}'
    qa_src_text,qa_trg_text=qa_matches2tags(cur_qa_matches,src_toks0,trg_toks0,prefix0)
    cur_dict["src"]={"text":qa_src_text,"ids":[i0]}
    cur_dict["trg"]={"text":qa_trg_text,"ids":[i0]}

    # cur_dict["src"]={"text":src_seg0,"ids":[i0]}
    # cur_dict["trg"]={"text":trg_seg0,"ids":[i0]}

    aligned_pairs.append(cur_dict)
  out_dict={"src":src_sents,"trg":trg_sents,"alignment":aligned_pairs}
  return out_dict




if __name__ == '__main__':
  from waitress import serve
  print("serving app")
  serve(app, host="0.0.0.0", port=4000)
  #app.run()
