#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
imageName = form.getvalue('imageName')
containerName = form.getvalue('containerName')
networkDriver = form.getvalue('networkDriver')
networkName = form.getvalue('networkName')
containerPortNumber = form.getvalue('containerPortNumber')
volume = form.getvalue('volume')

print(imageName," ",containerName," ",networkDriver," ",networkName," ",containerPortNumber," ",volume);

