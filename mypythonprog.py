#This program will read the .csv file and average the packets received

f= open("manet-routing.output.csv", "r")

lines = f.readlines()[101:] # Starts reading at line 101, ignors the first 100
accumulator = 0.0
for i in lines:
	i = i.replace(',', ' ')	# Removes the commma
	thisline = i.split()
	accumulator += float(thisline[1])	#Adds the second item in the row (Packets Received)

f.close()
accumulator =accumulator / 100
print(accumulator)	#This is the average packets received in the simulation

