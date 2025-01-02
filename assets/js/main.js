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
  cur_table.innerHTML=""
  align_output=res["align_output"] || {}
  aligned_pairs=align_output["alignment"] || []

  res_input_data=res["data"] || {}
  src_lang=res_input_data["src_lang"] || "en"
  trg_lang=res_input_data["trg_lang"] || "ar"

  counter0=0

  for (it0 of aligned_pairs){
    counter0+=1
    console.log(it0)
    var row = cur_table.insertRow(-1);
    row.className="odd:bg-white even:bg-sky-50"

    row.onclick=open_seg_pair

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    
    if (src_lang=="ar") {
      cell1.style.textAlign = "right";
      cell1.dir = 'rtl'
    } 
    if (trg_lang=="ar") {
      cell2.style.textAlign = "right";
      cell2.dir = 'rtl'
    } 

    cell1.setAttribute("name", "src_cell")
    cell2.setAttribute("name", "trg_cell")

    cell2.setAttribute("id", "trg_"+counter0)
    cell2.contentEditable=true;


    // Add some text to the new cells:
    cur_src=it0["src"] || {}
    cur_trg=it0["trg"] || {}
    src_ids=cur_src["ids"] || []
    trg_ids=cur_trg["ids"] || []
    cell1.innerHTML = cur_src["text"] || "" //"NEW CELL1";
    cell2.innerHTML = cur_trg["text"] || " " //"NEW CELL2";

    cell1.className="p-2"
    cell2.className="trg_segs p-2"

  }

}


function back2input(){
  $$("output_div").hidden=true;
  $$("input_div").hidden=false;

}

function open_seg_pair(evt){
  console.log(evt)
  evt_trg0=evt.currentTarget
  //src_cell = trg0.getElementsByName("src_cell");
  //trg_cell = trg0.getElementsByName("trg_cell");
  let src_cells = evt_trg0.querySelector("[name='src_cell']");
  let trg_cells = evt_trg0.querySelector("[name='trg_cell']");
  console.log(src_cells.innerHTML)
  console.log(trg_cells.innerHTML)
  //jQuery.noConflict(); 
  //$('#seg_pair_modal').modal('show');
  $$("seg_pair_modal_btn").click()

  $$("modal_src_seg").innerHTML=src_cells.innerHTML
  $$("modal_trg_seg").innerHTML=trg_cells.innerHTML
  $$("modal_trg_seg").dataset.trg=trg_cells.id

  //console.log(trg_cell)

}

function update_trg_seg(obj0){

  console.log(obj0)
  modal_trg_seg_el=$$("modal_trg_seg")
  corr_table_trg_el_id=modal_trg_seg_el.dataset.trg || ""
  console.log(modal_trg_seg_el)
  console.log(corr_table_trg_el_id)

}