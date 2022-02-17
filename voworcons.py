l = input("Enter a character: ")

if(l=='A' or l=='a' or l=='E' or l =='e' or l=='I'
 or l=='i' or l=='O' or l=='o' or l=='U' or l=='u'):
    print(l, "is a vowel")
elif(l=='Y' or l=='y'):
    print(l,"is both vowel and consonant")
    
else:
    print(l, "is a consonant")