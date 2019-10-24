import psutil
import time

def getMem(filename,upTime):
	a = psutil.virtual_memory()
	b=str(a.percent) + " " + str(upTime) + "\n"
	fhand.write(b)
	
filename = "Memory.txt"
fhand = open(filename,'w')

upTime = 0

while True:
	time.sleep(10)
	upTime = upTime + 10
	getMem(fhand,upTime)


	
