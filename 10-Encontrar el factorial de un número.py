def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numeros_a_probar = [22]

for numero in numeros_a_probar:
    print(f"Factorial de {numero} es: {factorial(numero)}")