const AVAILABLE_LANGUAGES = [
    ["한국어","Ko"],
    ["English", "En"]
  ]

  const DEFAULT = "Ko"
  var currentLang = DEFAULT

function generateSelectorHTML(){
  let op_array = new Array();

  for (let i = 0; i < AVAILABLE_LANGUAGES.length; i++) {
    op_array.push(AVAILABLE_LANGUAGES[i]);
  }
  let inner = op_array.map((elem)=> {return elem[1] == currentLang? `<option value="${elem[1]}" selected="selected">${elem[0]}</option>` : `<option value="${elem[1]}">${elem[0]}</option>`}).join(" ")
  return `<select class="lang_val"> ${inner} </select>`
}

function renderLanguageSelector(_lang_tag){
  let lang_html = generateSelectorHTML();
  $(_lang_tag).html(lang_html)

}

async function getLanguage(_lang_abbr) {
  console.log(_lang_abbr)
  let lang_struct = await $.ajax({url:`/language/${_lang_abbr}`,method:"GET"});
  return lang_struct;
}

async function switchLanguageOnView(_lang_abbr){
    let lang_struct = await getLanguage(_lang_abbr);
    let keys = Object.keys(lang_struct);

    for (let i = 0; i < keys.length; i++){
      let key = keys[i];
      let body = lang_struct[key];
      $(key).text(body);
    }

}

renderLanguageSelector(".lang_select");



$(document).ready(()=>{

  switchLanguageOnView(currentLang);

  $(".lang_val").on("change", function(){
    var select = $(this).val();
    switchLanguageOnView(select);
    currentLang = select;
  })

});
