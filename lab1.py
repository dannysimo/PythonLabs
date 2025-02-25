#Cerinta 3:
print("Hello Worold!")
name=input("Introduceti numele: ")
print(name)
#Cerinta 4:
vint=1
vfloat=2.5
vtext1="hello"
vtext2='''Defineste 4 variabile, folosind denumiri corecte pentru ele in Python.
Atribuie fiecarei dintre ele, pe rand:
o valoare intreaga numerica, o valore reala, o valoare text scurta, o valoare text care ocupa 3-4 randuri.'''
#Cerinta 5:
print(type(vint))
print(type(vfloat))
#Cerinta 6:
print(len(vtext1))
print(len(vtext2))
#Cerinta 7:
textup=vtext1.upper()
print(textup)
#Cerinta 8:
print(vtext2[63:70])
#Cerinta 10:
vtext3="Cantitate de cumprat:{},pretul:{} euro"
print(vtext3.format(vint,vfloat))
print(f"Cantitate de cumprat:{vint},pretul:{vfloat} euro")