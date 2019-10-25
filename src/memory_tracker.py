import psutil
import time

def getMem(filename,upTime):
	a = psutil.virtual_memory()
	b=str(a.percent) + " " + str(upTime) + "\n"
	fhand.write(b)
	
filename = "Memory.txt"
fhand = open(filename,'w')

upTime = 0
timeIncrement = input("Enter how many sec increment you want to use")
while True:
	time.sleep(int(timeIncrement))
	upTime = upTime + int(timeIncrement)
	getMem(fhand,upTime)


	
