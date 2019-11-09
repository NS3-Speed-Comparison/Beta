#This program will run the manet-routing-compare for the protocol and speed ranges
#Then it will write the results to the speed-comparison-results.csv file
import os

protocolRange = range(1, 5)
speedRange = range(0, 35, 5)

protocolNames = ["OLSR", "AODV", "DSDV" ,"DSR"]

outputFilePDR = open("speed-comparison-pdr.csv", "w")
outputFileDelay = open("speed-comparison-delay.csv", "w")

taskCount = 0;
totalCount = len(protocolRange) * len(speedRange);

outputFilePDR.write(",")
outputFileDelay.write(",")
for i in speedRange:
	outputFilePDR.write(str(i) + ",")
	outputFileDelay.write(str(i) + ",")
outputFilePDR.write("\n")
outputFileDelay.write("\n")

for i in protocolRange:
	print("Running Protocol: " + protocolNames[i-1])
	outputFilePDR.write(protocolNames[i-1] + ",");
	outputFileDelay.write(protocolNames[i-1] + ",");
	for j in speedRange:
		taskCount += 1
		print("Speed: " + str(j))
		os.system('./waf --run "scratch/manet-routing-compare --protocol=' + str(i) + ' --speed=' + str(j) + '.01"')
		f= open("manet-speed-result.csv", "r")
		lines = f.readlines()
		pdrLine = lines[1]
		delayLine = lines[3]
		pdr = pdrLine.split(",")[2][:-1]
		delay = delayLine.split(",")[2][:-1]
		outputFilePDR.write(pdr + ",")
		outputFileDelay.write(delay + ",")
		f.close()
		print("Packet Delivery Ratio: " + pdr)
		print("Average End-to-End Delay: " + delay)
		print("[" + str(taskCount) + "/" + str(totalCount) + "](" + str(int((float(taskCount) / totalCount)*100)) + "%)\n")
	outputFilePDR.write("\n")
	outputFileDelay.write("\n")

outputFilePDR.close()
outputFileDelay.close()
print("Speed Comparision Complete")