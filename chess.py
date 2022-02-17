h=input("Enter the height  ")
w=input("Enter the weight  ")
if(h=='a' or h=='A' or h=='c'or h=='C'or h=='e'or h=='E'or h=='g'or h=='G') and float(w)%2==1:
    print("The cell is black")
elif(h=='b' or h=='B' or h=='d'or h=='D'or h=='f'or h=='F'or h=='h'or h=='H') and float(w)%2==0:
     print("The cell is black")
else:
    print("The cell is white")