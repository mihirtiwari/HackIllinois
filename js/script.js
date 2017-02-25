function login() {
  var firstName = document.getElementById("firstName").value;
  firstName = firstName.replace(/\s+/g, '');

  var lastName = document.getElementById("lastName").value
  lastName = lastName.replace(/\s+/g, '');

  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://127.0.0.1:5000/taken/firstName=Jason&lastName=Argonaut", false);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();
  var response = JSON.parse(xhttp.responseText);

  console.log(response);

  saveName(firstName, lastName);
  document.location.href = 'index.html';
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
