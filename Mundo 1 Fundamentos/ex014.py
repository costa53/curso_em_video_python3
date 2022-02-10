# DESAFIO 014
# Escreva um programa que converta uma temperatura digitada em °C e a converta para °F.

c = float(input('Informe a temperatura em °C: '))
f = (c * 1.8) + 32
print(f'A temperatura de {c}°C corresponde a {f:.1f}°F!')
