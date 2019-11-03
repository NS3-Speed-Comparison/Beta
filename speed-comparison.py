#This program will run the manet-routing-compare for the protocol and speed ranges
#Then it will write the results to the speed-comparison-results.csv file
import os

protocolRange = range(1, 5)
speedRange = range(0, 35, 5)

protocolNames = ["OLSR", "AODV", "DSDV" ,"DSR"]

outputFile = open("speed-comparison-results.csv", "w")

taskCount = 0;
totalCount = len(protocolRange) * len(speedRange);

outputFile.write(",")
for i in speedRange:
	outputFile.write(str(i) + ",")
outputFile.write("\n")

for i in protocolRange:
	print("Running Protocol: " + protocolNames[i-1])
	outputFile.write(protocolNames[i-1] + ",");
	for j in speedRange:
		taskCount += 1
		print("Speed: " + str(j))
		os.system('./waf --run "scratch/manet-routing-compare --protocol=' + str(i) + ' --speed=' + str(j) + '.01"')
		f= open("manet-speed-result.csv", "r")
		line = f.readlines()[1]
		pdr = line.split(",")[2][:-1]
		outputFile.write(pdr + ",")
		f.close()
		print("Resulting PDR: " + pdr)
		print("[" + str(taskCount) + "/" + str(totalCount) + "](" + str(int((float(taskCount) / totalCount)*100)) + "%)\n")
	outputFile.write("\n");

outputFile.close()
print("Speed Comparision Complete")