#Cerinta(b)
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1[0],list1[4])
list1[1]=22
print(list1)
print(list1[0:2])
#1Metoda
list1.append(52)
print(list1)
#2Functii
x=len(list1)
print(x)
x1=max(list1)
print(x1)
#3Operatori
print(list1+list2)
print(list1<list2)
print(999 in list1)

#Cerinta(c)
tuplelist=("element1","element2","element3")
print(type(tuplelist))
print(tuplelist[0],tuplelist[2])
print(tuplelist[0:2])
x2=len(tuplelist)
print(x2)
x3=max(tuplelist)
print(x3)
x4=min(tuplelist)
print(x4)

#Cerinta(d)
set1={5,2,1,9,6,5,7,8,2}
print(set1)
set1.remove(2)
print(set1)
x=sum(set1)
print(x)

#Cerinta(e)
dict1={'Nume':"Barzan","Prenume":"Narzan","Patronimic":"Nikolaevici"}
print(dict1['Nume'])

dict2={1:"Unu",2:"Doi",3:"Trei"}
print(dict2[1])

#Cerinta(f)
tlist1=tuple(list1)
print(type(tlist1))

#2.a 
xlist=[6,10,30]
txlist=["Piine","Lapte","Oua"]
print(f"Lista de produse:{txlist[0]}:{xlist[0]} lei,{txlist[1]}:{xlist[1]} lei,{txlist[2]}:{xlist[2]} lei,")

#2.b 
v=input("Introduceti virsta:")
vint=int(v)
r=vint+5
print("In cinci ani veti avea:",r,"ani")

#2.c 
aaa=[1,2,3,4,5,6]
print(10 in aaa)
print(3 in aaa)
print(5 not in aaa)
print(0 not in aaa)