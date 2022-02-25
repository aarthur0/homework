#DOVE programming language 
#1.	Յուրաքանչյուր հրամանից,character-ից հետո դրվում ա space
#2.	Մի տողում մեկ հրաման կարանք գրենք
#3.	Յուրաքանչյուր փոփոխական նոր տողից ենք հայտարարում ու պիտի սկզբնարժեքավորենք
import sys
import math

f=open("text.txt")

for line  in f:
	lst=line.split()
	var = {} 
	         ##valuable dictionary
	
	if lst[0]=="say":  #say-printing a string
		print (lst[1:])

	if lst[0]=="new" and lst[2]=="=" : #new - declaring a variable
		var[lst[1]]=lst[3]
		if len(lst)>3:
			
			#adding

			try:
				if lst[4]=="+" and lst[0]=="new":
					summ= float(lst[3]) + float(lst[5])
					var[lst[1]]= summ

			except Exception:
				pass 

			#subtraction

			try:
				if lst[4]=="-" and lst[0]=="new":
					diff= float(lst[3]) - float(lst[5])
					var[lst[1]]= diff

			except Exception:
				pass

			#multiplication	

			try:
				if lst[4]=="*" and lst[0]=="new":
					mult= float(lst[3]) * float(lst[5])
					var[lst[1]]= mult

			except Exception:
				pass

				#division

			try:
				if lst[4]=="/" and lst[0]=="new":
					div= float(lst[3]) / float(lst[5])
					var[lst[1]]= div

			except Exception:
				pass

			#degree

			try:
				if lst[4]=="**" and lst[0]=="new":
					deg=float(lst[3]) ** float(lst[5])
					var[lst[1]]=deg

			except Exception:
				pass

			#square root

			try:
				if lst[4]=="root/2":  # number root/2 - square root of the number
					rt= math.sqrt(float(lst[3]))
					var[lst[1]]=rt

			except Exception:
				pass

			#factorial

			try:
				if lst[4]=="fact!": # number fact! - factorial of the number 
					fc=math.factorial(int(lst[3]))
					var[lst[1]]=fc

			except Exception:
				pass

			res=var|var
	
	#print(res)

	if lst[0]=="say>" and lst[1] in res.keys():#say> printing a variable
		print(res[lst[1]])

	if lst[0]=="floop" and lst[3]=="<->" and lst[5]=="[" and lst[8]=="]" and lst[1]==lst[7]:

		                                                         ##lst[1]-range start,lst[7]-range stop
		                                                         #for loop syntax - 
		                                       #floop x a(start number) <-> b(stop number) [ say> x] dolp 
		                                       #եթե ուզում ենք ավարտի աշխատանքը dolp-ի փոխարեն գրում ենք endlp
		                                       #ամբողջ floop-ը գրում ենք մի տողի վրա

		if lst[6]=="say>":

			for i in range(int(lst[2]),int(lst[4])+1):
				try:
					if (lst[9]=="dolp" ):
						print(i)
						
					elif lst[9]=="endlp":
						print("Loop end")
						break

				except Exception:
					pass

		print('\n')


			#using for in strings

		if lst[6]=="fsay>" and lst[2]==lst[4]=="str":  #fsay> - printing string characters in floop
			                                           #start-ի ու stop-ի համարների փոխարեն գրում ենք str

			for j in lst[1]:
				try:
					if lst[9]=="dolp":
						print(j)
					elif lst[9]=="endlp":
						print("Loop end")
						break
					else:
						print("Something went wrong\nTry again!")


				except Exception:
					pass

		print('\n')



	if lst[0]=="case" :                      #case - if
		                                     #syntax- case condition || execution

		if lst[1]=="true" and lst[2]=="||":
			if lst[3]=="say":
				print(lst[4:])
			else:
				print("Something went wrong\nTry again!")
		if lst[1]=="false" and lst[2]=="||":
			break
		if lst[2]=="<" and lst[4]=="||":
			try:
				if float(lst[1]) < float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass

		if lst[2]==">" and lst[4]=="||":
			try:
				if float(lst[1]) > float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass

		if lst[2]=="==" and lst[4]=="||":
			try:
				if float(lst[1]) == float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass

		if lst[2]=="!=" and lst[4]=="||":
			try:
				if float(lst[1]) != float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass

		if lst[2]=="<=" and lst[4]=="||":
			try:
				if float(lst[1]) <= float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass


		if lst[2]==">=" and lst[4]=="||":
			try:
				if float(lst[1]) >= float(lst[3]):
					if lst[5]=="say":
						print(lst[6:])
				else:
					print("Something went wrong\nTry again!")
			except Exception:
				pass









	
		
	
		

	