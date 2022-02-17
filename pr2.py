k=input
s=0
c=0

while k:
    k=input("Input a number ")
    if k== 'done' :
        break
    try:
        c=c+1
        s=s+float(k)
    except ValueError:
        print("Invalid input")
    
print(s," ",c," ",(s/c))