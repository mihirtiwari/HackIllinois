function checkMedication() {
  document.getElementById("alerts").innerHTML = "";   // Reset alerts to empty

  var drug = "";
  var substring = "";
  var newMedication = document.getElementById("search").value;

  // Loop through all the drugs and put into readable format for API, delimited by 0
  for (var i = 0; i < medication.length; i++) {
    if(i != medication.length - 1){
      drug += medication[i].substring(medication[i].indexOf("(") + 1, medication[i].indexOf(")")) + "0";

    } else {
      drug += medication[i].substring(medication[i].indexOf("(") + 1, medication[i].indexOf(")"));
    }
  }

  drug = drug.split(' ').join(','); //Replace spaces with commas

  // Send request for medication conflicts to servers
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://127.0.0.1:5000/combine/drug=" + drug + "&check_drug=" + newMedication, false);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();

  var response = JSON.parse(xhttp.responseText);
  var description = response.description;

  //Loop through object containing conflicts and generate alerts
  for (var key in description) {
    if (description.hasOwnProperty(key)) {
      generateAlert(key + ": " + description[key]);
    }
  }

}

// Generate card for current medication of patient
function generateCard(code, drug){
  var title = drug.substring(drug.indexOf("(") + 1, drug.indexOf(")"));
  var description = drug;
  var id = code;
  var card = "<div style=\"margin-top:20px; margin-right: 30px;\" class=\"card\"><div class=\"card-header\" style=\"background-color:#515151;color:white;\">" + code + "</div><div class=\"card-block\"><h3 class=\"card-title\">" + title + "</h3><p class=\"card-text\">" + description + "</p></div></div>";

  var div = document.getElementById("drugs");
  div.innerHTML += card;
}

// Generate alert for conflicts that might arise from new medication
function generateAlert(alertMessage){
  var alert = "<div class=\"alert alert-danger\" role=\"alert\" style=\"margin-top:50px; margin-left:10px;\"><strong>Careful! </strong>" + alertMessage + "</div>";

  var div = document.getElementById("alerts")
  div.innerHTML = div.innerHTML + alert;
}
