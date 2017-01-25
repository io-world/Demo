import xmlrpclib


# connect to the eggPlant instance

server = xmlrpclib.ServerProxy("http://127.0.0.1:5400")



# start the session

server.startsession("/Users/randyhesse/Documents/Demos/eggDrive.suite")


# connect eggPlant to the SUT

server.execute("connect serverId:\"172.16.229.129\", port:\"5900\", password:\"Spr1ng\"")



# run whatever eggPlant code you need/want to run

server.execute("click \"Chrome.png\"")
server.execute("doubleclick \"Chrome.png\"")
server.execute("moveto (400,200)")



##server.execute("runwithnewresults \"index\"")




# end the session

server.endsession("")