"""
Módulo de operaciones matemáticas básicas.
(En este estado inicial, las funciones están definidas pero sin implementar.)
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
