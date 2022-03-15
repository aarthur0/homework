import random
file=open("art.txt","w")
file.seek(1024*1024*1024*4)
for i in range(0,4000000000):
	file.write(str(random.randint(1, 120)))
	file.write("\n")
