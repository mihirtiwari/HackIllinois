function login() {
  var firstName = document.getElementById("firstName").value;
  firstName = firstName.replace(/\s+/g, '');

  var lastName = document.getElementById("lastName").value;
  lastName = lastName.replace(/\s+/g, '');

  try{
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:5000/taken/firstName=" + firstName + "&lastName=" + lastName, false);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
    var response = JSON.parse(xhttp.responseText);
    saveName(firstName, lastName);
    saveJSON(response);
    document.location.href = 'index.html';
  } catch (err) {
    document.location.href = 'error/503.html'
  }

}

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
