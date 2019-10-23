import psutil

def getMem(filename):
	a = psutil.virtual_memory()
	print(a.percent)
	b=str(a.percent) + "\n"
	fhand.write(b)
	
filename = "Memory.txt"
fhand = open(filename,'w')

while True:
	sleep(10)
	getMem(fhand)


	
