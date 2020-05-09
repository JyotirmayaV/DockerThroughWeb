#!/usr/bin/python3

import subprocess
print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
container = "sudo docker run -dit"

imageName = form.getvalue('imageName')

containerName = form.getvalue('containerName')

networkDriver = form.getvalue('networkDriver')

networkName = form.getvalue('networkName')

containerPortNumber = form.getvalue('containerPortNumber')

volume = form.getvalue('volume')


container = container + " --name " + str(containerName)    

if networkName is not None:
    mynetwork = "docker network create --drive " + str(networkDriver) + " " + str(networkName)
    container = container + " --network " + str(networkName)

if containerPortNumber is not None:
    container = container + " --p " + str(containerPortNumber) + ":80"

if volume is not None:
    container = container + " -v /lw:" + str(volume)

container = container + " "+str(imageName)

#print(subprocess.run('date'))

#print(container)

#subprocess.run(container,shell=True)

#print('success')
#print(subprocess.run('docker ps -a',shell=True))

#print(imageName," ",containerName," ",networkDriver," ",networkName," ",containerPortNumber," ",volume);
#print('erroring')

print(subprocess.getoutput('date'))

x = subprocess.getoutput(container)

print(x)

print('<pre>',subprocess.getoutput('sudo docker ps -a'),'</pre>')

print("man new problem every day annoys me")
