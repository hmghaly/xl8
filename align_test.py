from code_utils.general import *
from code_utils.parsing_lib import *
from code_utils.align_utils import *
from code_utils.dep_lib import *
from code_utils.arabic_lib import *

#!pip install transformers==3.1.0
import torch
import transformers
import itertools

from itertools import groupby
from collections import Counter
ar_counter_dict=load_counts("data/ar_count.txt", tmp_count_dict={})

def cur_ar_tok_fn(text):
  cur_toks=tok(text)
  return tok_ar(cur_toks,ar_counter_dict)


bert_model = transformers.BertModel.from_pretrained('bert-base-multilingual-cased')
bert_tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-multilingual-cased')



print("Hello")

src0="[RO] We demand that the parties to the conflict uphold their obligations under international humanitarian law, including by taking constant care to spare civilians, humanitarian workers and civilian objects from harm, and that they grant safe and unhindered access to humanitarian assistance for all in need."
trg0="[RO] نطالب أطراف النزاع بالوفاء بالتزاماتها بموجب القانون الدولي الإنساني، بما في ذلك الحرص الدائم على تجنيب المدنيين والعاملين في المجال الإنساني والأهداف المدنية الأذى، وأن تتيح الوصول الآمن ودون عوائق للمساعدات الإنسانية لجميع المحتاجين."

src_tokens0=tok(src0)
trg_tokens0=tok(trg0) #cur_ar_tok_fn(trg0)

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



bitext="""
loading completed
S.PV9734-021	S.PV9734-021		
HG/4	HG/4		
(Palestine)-A	(Palestine)-A		
Israel is continuing with its aggressive plan to drag the entire region into open warfare.	إن إسرائيل مستمرة في مخططها العدواني حتى تجر المنطقة بكاملها نحو حرب مفتوحة.		
Will the Security Council continue its traditional stance of condemnation and demands, expecting Israel to comply?	هل سيستمر مجلس الأمن في موقفه التقليدي الذي ينتهي بالتنديد والمطالبة، متوقعا من إسرائيل الامتثال؟		
When will members activate their tools here in the Security Council that compel Israel to comply in order to maintain and preserve international peace and security?	متى سيفعِّل الأعضاء * أدواتهم هنا في مجلس الأمن التي تجبر إسرائيل على الامتثال، لصون وحفظ على الأمن والسلم الدوليين؟		
How long will Chapter VII be forbidden for Israel?	إلى متى سيكون الفصل السابع محرماً على إسرائيل؟		
Are members waiting for a bigger disaster?	هل ينتظر الأعضاء كارثة أكبر من ذلك؟		
Are they waiting for a bigger war?	هل ينتظرون حرباً أوسع من ذلك؟		
We condemn the targeting of all civilians, regardless of their ethnicity, nationality or religion.	نحن ندين استهداف المدنيين كافة، وعلى السواء، مهما كان عرقهم أو جنسيتهم أو دينهم.		
There is no justification for targeting or harming civilians.	فلا يوجد مبرر يسمح أو يعطي أحدا ترخيصا لاستهداف المدنيين وإيقاع الأذى بهم.		
Perhaps what we can conclude with regard to the Palestinian question this week at the United Nations is that leaders of the world from different countries believe that it is illogical and even insane to continue with the same approach that we used in the past to face the enormous challenges we are facing today, which prevent us from achieving a just, comprehensive and lasting peace.	لعل ما يمكن استخلاصه فيما يخص القضية الفلسطينية خلال هذا الأسبوع من الوقت الذي قضيناه في الأمم المتحدة هو أن قادة العالم من مختلف بقاع الأرض يرون أنه من اللا منطقي، بل من الجنون أن نستمر على نفس النهج الذي اعتدنا عليه في الماضي لمواجهة التحديات المهولة التي نقف أمامها اليوم، والتي تمنعنا من تحقيق السلام العادل والشامل والدائم.		
That also means that it is not possible to merely express and join the consistent international position on the peaceful settlement of the Palestinian question and then leave things as they are until all the parties are ready to negotiate in favour of a just, peaceful and comprehensive solution.	ويعني ذلك أيضاً أنه من غير الممكن الاكتفاء فقط بالتعبير والانضمام إلى الموقف الدولي الثابت بشأن التسوية السلمية للقضية الفلسطينية، ثم ترك الأمور إلى أن يأتي الوقت الذي تصبح هذه الأطراف جاهزة للتفاوض من أجل التوصل إلى حل عادل وسلمي وشامل.		
We cannot ignore the fact that there is a party that does not want to negotiate, even though that party has all the time to do so and is imposing illegal facts on the ground, according to its internal and colonial political agenda, that are contrary to international law and the Charter of the United Nations.	فلا يمكن الآن تجاهل حقيقة أن هناك طرفاً لا يريد التفاوض، ولكنه من يملك الوقت كله ويفرض الحقائق غير الشرعية على الأرض، وفق أجندته السياسية الداخلية والاستعمارية، المنافية للقانون الدولي وميثاق الأمم المتحدة.		
At the same time, the other party is racing against time and with every passing day is losing what is most precious and valuable for which there is no compensation and which cannot be recovered.	وهناك طرف يسابق الزمن، يفقد في كل يوم ما هو أغلى وأثمن، وما لا يمكن تعويضه واستعادته.		
We can no longer believe that managing the conflict, instead of ending it, is a viable strategy that will lead to security and stability.	كما لا يمكن بعد اليوم التصديق بأن إدارة الصراع، بدلا من إنهائه، هي استراتيجية مجدية تصل بنا إلى الأمن والاستقرار.		
The consistent international positions on the peaceful settlement of the Palestinian question are necessary and very important positions that we have collectively worked on for decades so that they become internationally agreed terms of reference based on international law and the resolutions of international legitimacy.	إن المواقف الدولية الثابتة بشأن التسوية السلمية للقضية الفلسطينية هي مواقف ضرورية وهامة جداً، وقد سعينا معكم بشكل جماعي للتوصل إليها على مر العقود، لتصبح مرجعيات دولية متفق عليها وتستند إلى القانون الدولي وقرارات الشرعية الدولية.		
However, today we are facing great challenges and are at a historical juncture, and those positions alone are no longer sufficient.	ولكننا نقف الآن أمام تحديات عظيمة ومنعطف تاريخي، لم تعد هذه المواقف وحدها كافية.		
It has become urgent to redouble efforts to take practical measures to make ending the occupation and realizing the two-State solution, along the borders of 1967, a reality on the ground that cannot be revoked or retracted.	وأصبح من الملح أن تتكاتف الجهود لاتخاذ إجراءات عملية تجعل من إنهاء الاحتلال وتنفيذ حل الدولتين، على حدود عام 1967، حقيقة وتمارس على الأرض الواقعية لا يمكن إبطالها أو التراجع عنها.		
It cannot remain merely an international political or security vision.	ولا يمكن الإبقاء عليها كمجرد رؤية سياسية أو أمنية دولية.		
With every new Palestinian generation, Israel, the illegal occupation authority, deliberately tries to destroy Palestine.	مع ظهور جيل فلسطيني جديد، تتعمد إسرائيل، سلطة الاحتلال غير الشرعية، تدمير فلسطين.		
We rebuild it, but Israel destroys it again.	ثم نعيد بناءها، ثم تدمرها مرة أخرى.		
We rebuild it again, and it is destroyed again.	ونعيد بناءها مرة أخرى، ثم تُدمَر مرة أخرى.		
We have experienced great hardships and many tragedies, and our people have managed to lift themselves up after each tragedy, healing their wounds, bearing their pain, holding on to their hope and determined to live.	لقد مررنا بمحن ومآسٍ شتى، ونهض شعبنا بعد كل محنة ململما جراحه، حاملا ألمه، وحافظا أمله، مصمما على الحياة.		
Our people deserve the Council’s support, solidarity, help and assistance.	مستحقا لدعم المجلس وتضامنه ومؤازرته ومساندته التي يقدمها.		
Every time, the Palestinian building and development machine is met with the Israeli demolition and destruction machine.	في كل مرة، آلة البناء والتطوير الفلسطينية تُقابَل بآلة التدمير والهدم الإسرائيلية.		
We build and Israel destroys.	نحن وأنتم نبني وإسرائيل تدمر.		
We build schools and raise human beings, and Israel demolishes schools and executes human beings.	نبني المدرسة والإنسان، وإسرائيل تهدم المدرسة وتعدم الإنسان.		
We want to rebuild Palestine in a way that guarantees that it will not be destroyed again, that our people will not be displaced once again and not stand at the doors of the Security Council grieving and crying for help once again.	نريد إعادة بناء فلسطين بشكل يضمن ألا تتعرض للتدمير مرة أخرى، ولا يجبر شعبنا على النزوح قسرا مرة أخرى، وألا يقف على أبواب مجلس الأمن مكلوما مرة أخرى.		
We want to rebuild Palestine with the certainty that its path will lead it forward towards prosperity, where its people can live in dignity in a sovereign State among States and as a free nation among nations.	نريد أن نعيد بناء فلسطين ونحن على يقين بأن الطريق الذي ينتظرها هو الطريق الذي يأخذها نحو الأمام نحو الازدهار، يعيش شعبنا فيها بكرامة كدولة ذات سيادة بين الدول وكأمة حرة بين الأمم.		
We want to be free from the illegal Israeli occupation without delay, in accordance with the advisory opinion of the International Court of Justice on the Legal consequences arising from the policies and practices of Israel in the occupied Palestinian territory, including East Jerusalem.	نريد الانعتاق من الاحتلال الإسرائيلي غير القانوني دون أي تأخير، وفق فتوى محكمة العدل الدولية بشأن الآثار القانونية الناشئة عن سياسات إسرائيل وممارساتها في الأرض الفلسطينية المحتلة، بما فيها القدس الشرقية.		
We want our free and sovereign independent State, with East Jerusalem as its capital.	نريد دولتنا المستقلة، وعاصمتها القدس الشرقية، حرة ذات سيادة.		
We want our people to live on their own land, enjoying freedom and dignity, guaranteed by their legitimate right to self-determination, without delay.	نريد لشعبنا أن يعيش على أرضه ينعم فيها بالحرية والكرامة كما يكفله له حقه المشروع في تقرير المصير دون أي تأجيل.		
We have all the necessary ingredients, namely, history, heritage, civilization, experience, capability and will, and most importantly, we have the resilient and capable Palestinians, who are our inexhaustible human resources.	فنحن لدينا المكونات اللازمة، لدينا التاريخ والإرث والحضارة، لدينا التجربة والخبرة  والكفاءة، ولدينا القدرة والإرادة، والأهم من ذلك لدينا الإنسان، الإنسان الفلسطيني المثابر والقادر، هو ذخيرتنا وموردنا الذي لا ينضب.		
I would like to continue in English so that I can clarify some thoughts.	أود أن ألقي بقية كلمتي باللغة الإنكليزية حتى أوضح بعض الأفكار.		
(spoke in English)	(تكلم بالإنكليزية)		
We came here with a simple message: there must be no complicity and no complacency, no bias and no double standards, no excuses and no self-inflicted powerlessness.	لقد جئنا إلى هنا برسالة بسيطة: يجب ألا يكون هناك تواطؤ ولا تهاون، ولا تحيز ولا معايير مزدوجة، ولا أعذار ولا عجز ذاتي *.		
We call for the rule of international law for the benefit of all.	إننا ندعو إلى سيادة القانون الدولي لصالح الجميع.		
No country should be above the law.	لا ينبغي أن يكون أي بلد فوق القانون.		
No people should be denied the protection of the law.	لا ينبغي حرمان أي شخص من الحماية التي يكفلها * القانون.		
There must be no weapons to kill us, no trade with settlements and their associated regime to rob our land and resources.	يجب عدم السماح بالأسلحة لقتلنا *، ولا بالتجارة مع المستوطنات والنظام المرتبط بها لسرقة أرضنا ومواردنا.		
Israel must be held accountable rather than shielded while it continues committing its crimes.	يجب محاسبة إسرائيل بدلاً من حمايتها بينما تواصل ارتكاب جرائمها.		
Israel has a plan — it is not hiding it — to get rid of the Palestinian people and grab their land.	ولدى إسرائيل خطة - لا تخفيها - للتخلص من الشعب الفلسطيني والاستيلاء على أرضه.		
We need an international plan with the necessary measures to change the reality on the ground.	إننا بحاجة إلى خطة دولية تتضمن التدابير اللازمة لتغيير الواقع على الأرض.		
What we are calling for is clear.	وما ندعو إليه واضح.		
First, the State of Palestine must be recognized and its membership to the United Nations must be supported.	أولاً، يجب الاعتراف بدولة فلسطين ودعم عضويتها في الأمم المتحدة.		
Secondly, the advisory opinion of the International Court of Justice and General Assembly resolution ES-10/24 endorsing it must be implemented and Member States must demand an end to the unlawful Israeli presence in the entirety of the occupied Palestinian territory within 12 months.	وثانيا، يجب تنفيذ فتوى محكمة العدل الدولية وقرار الجمعية العامة دإط-10/24 الذي يؤيدها، ويجب على الدول الأعضاء المطالبة بإنهاء الوجود الإسرائيلي غير القانوني في كامل الأرض الفلسطينية المحتلة في غضون 12 شهرا.		
Thirdly, Member States should join the global alliance unveiled yesterday to end the occupation and achieve the independence of the State of Palestine and implement the two-State solution.	ثالثاً، ينبغي للدول الأعضاء الانضمام إلى التحالف العالمي الذي تم الكشف عنه بالأمس لإنهاء الاحتلال وتحقيق استقلال دولة فلسطين وتنفيذ حل الدولتين.		
Fourthly, we call on Member States to support our national plan Build Palestine, including to build our economy and consolidate our institutions.	رابعا، ندعو الدول الأعضاء إلى دعم خطتنا الوطنية لبناء فلسطين، بما في ذلك بناء اقتصادنا وتوطيد مؤسساتنا.		
If impunity ends, the Israeli occupation will end.	وإذا انتهى الإفلات من العقاب، سينتهي الاحتلال الإسرائيلي.		
If the Israeli occupation ends, we will achieve shared peace and security.	وإذا انتهى الاحتلال الإسرائيلي، فسوف نحقق السلام والأمن المشترك.		
A free Palestine is the sole key that can unlock a peaceful future for our region and unleash its potential.	ففلسطين الحرة هي المفتاح الوحيد الذي يمكن أن يفتح مستقبلا سلميا لمنطقتنا ويطلق العنان لإمكاناتها.		
Everything else has been tried and failed.	لقد تم * تجربة كل شيء آخر وفشل.		
And the cost of that failure is measured in human lives, all too often in Palestinian lives.	وتكلفة هذا الفشل تقاس بالأرواح البشرية، وغالبا ما تكون أرواح الفلسطينيين.		
A different future is possible.	ولكن من الممكن إيجاد مستقبل مختلف.		
It starts with the decisions each State will make today.	ويبدأ الأمر بالقرارات التي ستتخذها كل دولة اليوم.		
The President: I now give the floor to the representative of Israel.	الرئيس (تكلم بالإنكليزية): أعطي الكلمة الآن لممثل إسرائيل.		
Mr. Danon (Israel): First, we cannot overlook Hizbullah’s recent actions.	السيد دانون (إسرائيل) (تكلم بالإنكليزية): أولاً، لا يمكننا التغاضي عن أعمال حزب الله الأخيرة.		
Since 8 October 2023, Hizbullah has launched over 9,000 rockets, more than 1000 anti-tank missiles and hundreds of explosive uncrewed aerial vehicles at the Israeli civilians.	فمنذ 8 تشرين الأول/أكتوبر 2023، أطلق حزب الله أكثر من 9 000 صاروخ، وأكثر من 1000 صاروخ مضاد للدبابات ومئات من الطائرات المسيرة المتفجرة على المدنيين الإسرائيليين.		
While we are interested in a diplomatic solution, we will take all necessary measures to ensure the safe return of the 70,000 internal refugees to their homes.	وفي حين أننا مهتمون بالحل الدبلوماسي، فإننا سنتخذ جميع التدابير اللازمة لضمان العودة الآمنة للاجئين الداخليين البالغ عددهم 70 000 شخص إلى ديارهم.		
It is time to hold Iran and its proxy accountable and take decisive action.	وقد حان الوقت لمحاسبة إيران ووكلائها واتخاذ إجراءات حاسمة.		
This is now our fifth meeting in the span of just 12 days.	هذه هي جلستنا الخامسة في غضون 12 يوماً فقط.		
How long will we repeat these debates?	إلى متى سنظل نكرر هذه المناقشات؟		
It is time for the Security Council to break free from the gridlock and regain a semblance of productivity.	لقد حان الوقت لكي يتحرر مجلس الأمن من حالة الجمود ويستعيد ما يشبه الإنتاجية *.		
We sit here today just 10 days from the one-year commemoration of the 7 October 2023 massacre, a day forever etched in the hearts of every Israeli.	إننا نجلس هنا اليوم قبل 10 أيام فقط من إحياء ذكرى مرور عام على مذبحة 7 تشرين الأول/أكتوبر 2023، وهو يوم محفور في قلب كل إسرائيلي إلى الأبد.		
More than 1,200 innocent lives were brutally taken in a single day.	تم إزهاق أكثر من 1 200 من الأرواح البريئة بوحشية في يوم واحد.		
[RO] People were...	[RO] People were...		
"""

print(bitext.split("\n"))