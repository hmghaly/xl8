function init(){
	console.log("Hello")
}

async function submit_analyze(){
  lang_form_dict= await get_form_vals("lang_input_form")
  console.log(lang_form_dict)	
  res=await post_data_async("align_api",lang_form_dict)
  console.log(res)
  $$("output_div").hidden=false;
  $$("input_div").hidden=true;
  //populate table
  cur_table=$$("bitext_table")
  align_output=res["align_output"] || {}
  aligned_pairs=align_output["alignment"] || []
  for (it0 of aligned_pairs){
    console.log(it0)
  }

}


function back2input(){
  $$("output_div").hidden=true;
  $$("input_div").hidden=false;

}