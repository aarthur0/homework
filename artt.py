file=open("art.txt","r")#արդեն գեներացված ֆայլ
fsplit1=open("split1.txt","x")#new files
fsplit3=open("split3.txt","x")
fsplit4=open("split4.txt","x")
fsplit5=open("split5.txt","x")
fsplit6=open("split6.txt","x")
fsplit7=open("split7.txt","x")
fsplit8=open("split8.txt","x")
fsplit9=open("split9.txt","x")
fsplit10=open("split10.txt","x")
fsplit11=open("split11.txt","x")
fsplit12=open("split12.txt","x")
fsplit13=open("split13.txt","x")
fsplit14=open("split14.txt","x")
fsplit15=open("split15.txt","x")
fsplit16=open("split16.txt","x")
fsplit17=open("split17.txt","x")
fsplit18=open("split18.txt","x")
fsplit19=open("split19.txt","x")
fsplit20=open("split20.txt","x")

lst=[]
for i in file:
	lst=i.split()
lst=[int(j) for j in lst]
k1=lst[0:20000]
k1.sort()
fsplit1.write(str(k1))
k2=lst[20001:40000]
k2.sort()
fsplit2.write(str(k2))
k3=lst[40001:60000]
k3.sort()
fsplit3.write(str(k3))
k4=lst[60001:80000]
k4.sort()
fsplit4.write(str(k4))
k5=lst[80001:100000]
k5.sort()
fsplit5.write(str(k5))
k6=lst[100001:120000]
k6.sort()
fsplit6.write(str(k6))
k7=lst[120001:140000]
k7.sort()
fsplit7.write(str(k7))
k8=lst[140001:160000]
k8.sort()
fsplit8.write(str(k8))
k9=lst[60001:80000]
k9.sort()
fsplit9.write(str(k9))
k10=lst[180001:200000]
k10.sort()
fsplit10.write(str(k10))
k11=lst[200001:220000]
k11.sort()
fsplit11.write(str(k11))
k12=lst[220001:240000]
k12.sort()
fsplit12.write(str(k12))
k13=lst[240001:260000]
k13.sort()
fsplit13.write(str(k13))
k14=lst[260001:280000]
k14.sort()
fsplit14.write(str(k14))
k15=lst[280001:300000]
k15.sort()
fsplit15.write(str(k15))
k16=lst[300001:320000]
k16.sort()
fsplit16.write(str(k16))
k17=lst[320001:340000]
k17.sort()
fsplit17.write(str(k17))
k18=lst[340001:360000]
k18.sort()
fsplit8.write(str(k18))
k19=lst[360001:380000]
k19.sort()
fsplit19.write(str(k19))
k20=lst[380001:400000]
k20.sort()
fsplit20.write(str(k20))

		

	