#1
greet_user = lambda name : print('Hello My Dear, ', name)
user_name = input("What is your name? ")
greet_user(user_name)
#2
tuplelist = [(3, 7), (1, 9), (4, 8), (2, 7), (5, 10), (13, 17), (11, 6)]
lista_sortata = sorted(tuplelist, key=lambda x: x[1])
print(lista_sortata)

#3
x=lambda n:2*n 
print(x(20))
#4
def salut():
 print("Salut!")
salut()

def salut1(nume):
 print(f"Salut,{nume}")
salut1("Jora")

def salut2(nume="Barzan",familie="Nikolaevici"):
 print(f"{nume} {familie}?")
salut2()

def suma(a,b):
 return a+b 
c=suma(5,4)
print(c)

def suma1(a,b):
 x=a+b 
 print(f"Suma={x}")
suma1(2,9)