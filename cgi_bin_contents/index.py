#!/usr/bin/python3

import subprocess as sb
print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields


def displayPage():

	#the starting tags
	print('''
	<html>
		
		<head>
			<title>
				My Docker World
			</title>
		</head>

		<body>

			<center><img src='docker.png' alt='Docker Logo'/>

			<h2>Welcome to Your One Stop Graphic Docker Management Environment</h2></center>

			<form action = 'index.py'>

			<pre>
			''')

	docker_containers = sb.getoutput('sudo docker ps -a')
		
	docker_containers = docker_containers + "\n"	
	
	length = len(docker_containers)

	start_index = 0

	end_index = docker_containers.find('\n')   #Because docker ps -a uses '\n' for next line of information display
	
	#print('first find : ',end_index,'..',docker_containers[end_index],'@')	
	
	print('      ',docker_containers[start_index:end_index] )   #printing the heading

	#start_index = end_index + 1 #skipped '\n'

	#print('start_index : ',start_index,'..',docker_containers[start_index],'@')

	docker_containers =  docker_containers[ end_index + 1 : length ] 
	
	length = len(docker_containers)
	
	#print("-----------------------------")
	#print(docker_containers)
	#print("-------------------------------")

	f = 1
	
	#start_index = 0	
	#print('next start_index : ',start_index,'..',docker_containers[start_index],'@')
	

	'''for i in repr(docker_containers):
		print(i)'''
	end_index = docker_containers.find('\n')
	#print('second find end_index : ',end_index)

	while True  :   
		#because at end when '\n' will not be found start_index will become 0 as start_index = end_index + 1 = -1 + 1 = 0
		
		#print(start_index," - ",end_index)	
		#print("***",docker_containers[start_index],"***")
		#print("###",docker_containers[start_index],"###")	

		print('''<br><input type="radio" name="containerID" value="{}"  {}>'''.format(docker_containers[ start_index : docker_containers.find(' ')] ,'checked' if f == 1 else ' ' ) ,end='')
		                
		print(docker_containers[ start_index : end_index ] )
		
		docker_containers =  docker_containers[ end_index + 1: length ] 
		
		start_index = 0
		end_index = docker_containers.find('\n')
		length = len(docker_containers)
		#print('new end index : ',end_index)
		
		#print()
		
		if end_index == -1 or end_index >= length :
			print(' end_index : ',end_index)
			print(' length : ',length,'good bye')
			break
		f = 2

		'''if f>=7 :
			print(start_index," - ",end_index," - ",length)
			break'''

	print('''
			<br>
			<button type='submit' onClick = "deleteSelected()" >Delete Container</button>  <button type='button' onclick = "seeCompleteDetails()" >Inspect Container</button>  <button type='button' onclick = "createImage()" >Create image of Container</button><br>

			<button type='button' onclick = "deleteAll()">Delete all Containers</button>
			<button type='button' onclick = "createNew()">Create a New Container</button>

		''')

	#the ending tags			
	print('''</pre>
			</form>



		</body>
	</html>
		
		''')


def deleteSelected():
	print("I am here in deleteSelected")

def seeCompleteDetails():
	print("I am here in seeCompleteDetails")

def createImage():
	print("I am here in createImage")

def deleteAll():
	print("I am here in deleteAll(")

def deleteAll():
	print("I am here in deleteAll")

def createNew():
	print("I am here in createNew")

displayPage()
'''container = "sudo docker run -dit"

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

print("man new problem every day annoys me")'''
