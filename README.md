# Prescription Merge Conflict (PMC)
The PMC is able to pull up a patient's past medication history in order to analyze whether a new medication will cause adverse interactions with current medication.

## Installation
Install pip and Python 2.7

### Prerequesites
#### Libraries
A requirments.txt file has been provided to download all of the required python libraries 3
Download required libraries with the following command
<br>
run the following command
<pre>pip install -r requirments.txt</pre>

## Usage
To run the flask server run the following command
<pre>python app.py</pre>
1. Everytime a change is made to any file the server is updated automatically
<br>
2. In order to stop the server <kbd>CTRL</kbd>+<kbd>C</kbd>
<br>
3. You can verify the server is runniong by going to http://127.0.0.1:5000 and looking for Hello World!
<br>
4. In order to view the website open the login.html file with a browser of your choice

## API Endpoints
####/taken/firstName=<firstName>&lastName=<lastName>
<strong>Description:</strong> Takes name of patient and returns an array of the names of medication being taken and their lexicographical codes
<br>
<strong>Method:</strong> GET
<br>
####/combine/drug=<drug>&check_drug=<check_drug>
<strong>Description:</strong> Takes all currently prescribed medication and newly proposed medication and returns the descriptions of their potential interactions
<br>
<strong>Method:</strong> GET
<br>
<strong>NOTE:</strong> When entering in drug names seperate current drug names by 0

## Contributors
Link to Contributors: <a href="CONTRIBUTORS.md">CONTRIBUTORS.md</a>
<br>
Link to Contributing: <a href="CONTRIBUTING.md">CONTRIBUTING.md</a>
