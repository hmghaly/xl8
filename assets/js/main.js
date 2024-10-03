function init(){
	console.log("Hello")
}

async function submit_texts(){
  lang_form_dict= await get_form_vals("lang_input_form")
  console.log(lang_form_dict)	

}