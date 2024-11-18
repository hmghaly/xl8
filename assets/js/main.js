function init(){
	console.log("Hello")
}

async function submit_analyze(){
  lang_form_dict= await get_form_vals("lang_input_form")
  console.log(lang_form_dict)	
  res=await post_data_async("align_api",lang_form_dict)
  console.log(res)

}