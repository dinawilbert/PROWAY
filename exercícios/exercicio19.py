"""
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio 
R. A fórmula para calcular o volume é: (4/3) * pi * R^3. Considere (atribua) para pi o valor 3.14159.

input = raio
processamento = (4/3) * 3.14159 * R^3
saida = volume

"""
raio = float(input("digite o valor do raio: "))
volume = (4 / 3) * 3.14159 * raio ** 3
print(f"o volume da esfera é: {volume:.2f}")