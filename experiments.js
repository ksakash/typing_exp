const input = document.querySelector('.input-to-copy');
const paragraph = document.querySelector('.p-to-copy-to');
const divText = document.querySelector('.c1');
const written_text = "Some use JavaScript, which may sometimes be preferable (literally adding a character at a time feels more like a real typewriter) and sometimes not be (potential accessibility concerns).";

let placeholder_value = "no value";
var completed = "";
const wrongSet = new Set();

var cursor = 0;

// document.addEventListener("keypress", typingFunction);
// window.addEventListener("keypress", typingFunction);

document.addEventListener("keyup", function(e) {
// function typingFunction(e) {
  // paragraph.innerText  = input.value;
  var input_char = e.key;
  txtlen = input.value.length;
  var left = written_text;
  var wrong = "";
  var was_wrong = false;

  if (input_char === written_text.charAt(cursor)) {
    cursor = cursor + 1;
  }
  else {
    wrongSet.add(cursor);
    was_wrong = true;
  }

  if (was_wrong) {
    left = written_text.slice(cursor+1, written_text.len);
  }
  else {
    left = written_text.slice(cursor, written_text.len);
  }

  let color;
  if (txtlen % 2 === 1) {
    color = "red";
  }
  else {
    color = "green";
  }
  var input_val = input.value.slice(0,txtlen/2);

  var prev_pos = 0;
  var completed_txt = "";

  for (let pos of wrongSet) {
    txt = written_text.slice(prev_pos, pos);
    completed_txt += "<span style=\"color:black\">" + txt + "</span>";
    completed_txt += "<span style=\"color:red\">" + written_text.charAt(pos) + "</span>";
    prev_pos = pos+1;
  }

  completed_txt += "<span style=\"color:black\">" + written_text.slice(prev_pos, cursor) + "</span>";

  s1 = "<span style=\"color:grey\">" + left + "</span>";
  // s2 = "<span style=\"color:black\">" + completed + "</span>";
  s = completed_txt + s1;


  divText.innerHTML = s;
  // placeholder_value = input.value[txtlen-1];
  placeholder_value = input_char;
});

document.querySelector('.button-container').addEventListener('click', function(event) {
  alert(`The entered value is ${placeholder_value}`)
});
