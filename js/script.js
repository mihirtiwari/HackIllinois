function saveName(firstName, lastName) {
  var name = {
   First: firstName,
   Last: lastName
  };

  name = JSON.stringify(name);
  name = btoa(name);
  localStorage.setItem('_name', name);
}

function saveJSON(json) {
  var j = JSON.stringify(json);
  j = btoa(j);
  localStorage.setItem('_drugs', j);
}

function generateCard(code, drug){
  var title = drug.substring(drug.indexOf("(") + 1, drug.indexOf(")"));
  var description = drug;
  var id = code;
  var card = "<div style=\"margin-top:20px; margin-right: 30px;\" class=\"card\"><div class=\"card-header\" style=\"background-color:#515151;color:white;\">" + code + "</div><div class=\"card-block\"><h3 class=\"card-title\">" + title + "</h3><p class=\"card-text\">" + description + "</p></div></div>";

  var div = document.getElementById("drugs");
  div.innerHTML += card;
}

function generateAlert(alertMessage){
  var alert = "<div class=\"alert alert-danger\" role=\"alert\" style=\"margin-top:50px; margin-left:10px;\"><strong>Careful! </strong>" + alertMessage + "</div>";

  var div = document.getElementById("alerts")
  div.innerHTML = div.innerHTML + alert;
}
