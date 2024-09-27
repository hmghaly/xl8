from code_utils.general import *
from code_utils.parsing_lib import *
from code_utils.align_utils import *
from code_utils.dep_lib import *
#!pip install transformers==3.1.0
import torch
import transformers
import itertools

bert_model = transformers.BertModel.from_pretrained('bert-base-multilingual-cased')
bert_tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-multilingual-cased')



print("Hello")

src0="[RO] We demand that the parties to the conflict uphold their obligations under international humanitarian law, including by taking constant care to spare civilians, humanitarian workers and civilian objects from harm, and that they grant safe and unhindered access to humanitarian assistance for all in need."
trg0="[RO] نطالب أطراف النزاع بالوفاء بالتزاماتها بموجب القانون الدولي الإنساني، بما في ذلك الحرص الدائم على تجنيب المدنيين والعاملين في المجال الإنساني والأهداف المدنية الأذى، وأن تتيح الوصول الآمن ودون عوائق للمساعدات الإنسانية لجميع المحتاجين."

src_tokens0=tok(src0)
trg_tokens0=tok(trg0)

align_out=bert_walign(src_tokens0,trg_tokens0,bert_tokenizer,bert_model)
#print(align_out)
aligned_phrases=present_aligned(src_tokens0,trg_tokens0,align_out)
for al_ph0 in aligned_phrases:
	print(al_ph0)
# for align_item0 in align_out:
# 	print(align_item0)

print("------")

conll_list=get_conll(src0)
# for a in conll_list:
# 	print("\t".join([str(v) for v in a]))
#print(conll_list)

phrases_obj=dep2phrases(conll_list)
phrase_info=phrases_obj["phrase_info"]
for ph_id0,ph_info0 in phrase_info.items(): 
	if not ph_id0.startswith("NP"): continue
	print(ph_id0)
	print(ph_info0)
	print("----")

