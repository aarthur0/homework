def split(word):
	return[i for i in word]
#word=input("Enter the word  ")
word='homos'
word=word.lower()
#print(split(word)[0])
_dict=['word','world','work','dogma','dog','do','origin','original','for','forecast',
'force','home','homo','cat','mouth','mouse','young','yoga','keep','welcome','know'
'well','butter','button','dance','jump','jungle','ape','phone','elephant','eagle',
'great','google','ice','island','logo','live','nut','night','queen','quit',
'rat','rabbit','rare','sleep','sink','tooth','text','use','until','value',
'view','xerox','zoo','able','bat','add','pencil','frog','language',
'large','mad','node','never','safe','drug','volume','pray','face','high',
'big','orange','create','cool','date','hour','clock','fool','true','age','eight',
'instead','door','leg','free','good','break','bus','camel','hand','culture',
'wrong','lip','drone','screen','close','mirror','light','ring','nail','end']
try:
	for i in _dict:
		if(word==i):
			print('The searched word',word, 'is in dictionary')
			quit()
	for j in _dict:
		if ( len(split(word))>=3 and (split(word)[0]==split(j)[0] and split(word)[1]==split(j)[1] and split(word)[2]==split(j)[2]  )):
			print("Did you mean",j)
			#at first suggests most similar words and then so on
		elif(len(split(word))>=2 and (split(word)[0]==split(j)[0] and split(word)[1]==split(j)[1]) ):
			print("Did you mean",j)
		elif(split(word)[0]==split(j)[0]):
			print("Did you mean",j)
			
	
except Exception:
	pass