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
    var row = cur_table.insertRow(-1);
    row.className="odd:bg-white even:bg-gray-50"

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);

    // Add some text to the new cells:
    cell1.innerHTML = "NEW CELL1";
    cell2.innerHTML = "NEW CELL2";

  }

}


function back2input(){
  $$("output_div").hidden=true;
  $$("input_div").hidden=false;

}