## Cómo ejecutar
python src/main.py
src/operaciones.py
"""
Módulo de operaciones matemáticas básicas.
(En este estado inicial, las funciones están definidas pero sin implementar.)

1º Estado actualizado.
2º Estado actualizado por segunda vez.

"""
def sumar(a, b):
 """Devuelve la suma de a y b."""
 return a + b
def restar(a, b):
 """Devuelve la resta de a y b."""
 return a - b

def multiplicar(a, b):
 """Devuelve la multiplicación de a por b."""

 return a * b
def dividir(a, b):

 """Devuelve la división de a entre b."""

 if b == 0:
 raise ValueError("No se puede dividir entre cero.")

 return a / b

src/main.py

from operaciones import sumar, restar, multiplicar, dividir

def mostrar_menu():

 print("\n=== CALCULADORA BÁSICA ===")

 print("1. Sumar"print("2. Restar")

 print("3. Multiplicar")

 print("4. Dividir")

 print("5. Salir")

def pedir_numero(mensaje):

 while True:

 try:

 return float(input(mensaje))

 except ValueError:

 print("Error: debes introducir un número válido.")

def main():

 while True:

 mostrar_menu()

 opcion = input("Elige una opción: ")
 if opcion == "1":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {sumar(a, b)}")
 elif opcion == "2":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {restar(a, b)}")
 elif opcion == "3":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {multiplicar(a, b)}")
 elif opcion == "4":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
try:
 print(f"Resultado: {dividir(a, b)}")
 except ValueError as e:
 print(f"Error: {e}")
 elif opcion == "5":
 print("Saliendo del programa...")
 break
 else:
 print("Opción no válida. Inténtalo de nuevo.")
