from datetime import datetime
current_year= datetime.now().year



y=int(input("Ingresa el primer numero "))
x=int(input("Ingresa el segundo numero "))
print("La suma es: %d" %(x+y))
print(f"la suma es: ",(x+y))
 
z=int(input("Ingresa el número: "))
if z%2==0:
    print("El número es par")
else:
    print("El número es impar")
 
name=str(input("Ingresa tu nombre "))
age=int(input("Ingresa tu edad "))
print(f"Hola: {name} en 10 años tendrás:  {age+10} naciste el años {current_year-age}")
 

x=int(input("Ingresa número: "))
y=int(input("Ingresa número: "))
z=int(input("Ingresa número: "))

#número mayor

if x>=y and x>=z:
    print(f"El número mayor es: {x}")
elif y>=x and y>=z:
    print(f"El número mayor es: {y}")
else:
    print(f"El número mayor es: {z}")


#numero menor
if x<=y and x<=z:
    print(f"El número menor es {x}")
elif y<=x and y<=z:
    print(f"El número menor es {y}")
else:
    print(f"El número menor es {z}")
 
menor = min(x, y, z)
mayor = max(x, y, z)
medio = x + y + z - menor - mayor
 
numeros=[x,y,z]
numeros.sort()
print(f"Organizados de menor a mayor: {numeros}")
 
word=input("Ingresa palabra ")

word_2=word[::-1]

if word_2 == word:
    print("Tu palabra es palíndromo")
else:
    print("La palabra no es palíndromo")
 
#Proyecto simulador de gastos
gastos = []

while True:
    dato = float(input("Ingresa tus gastos (0 para terminar): "))
    if dato == 0:
        break
    gastos.append(dato)

print("Mostrando los gastos almacenados")
for gasto in gastos:
    print(gasto)

print(f"Total gastado: {sum(gastos)}")
print(f"Gasto más alto:{max(gastos)}")
print(f"Gasto más bajo: {min(gastos)}")


