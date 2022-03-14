import random
file=open("art.txt","w")
for i in range(0,4000000000):
	file.write(str(random.randint(1, 120)))
	file.write("\n")
