faturamento = {1: 22174.1664, 2: 24537.6698, 3: 26139.6134, 4: 0.0, 5: 0.0,
               6: 26742.6612, 7: 0.0, 8: 42889.2258, 9: 46251.174, 10: 11191.4722,
               11: 0.0, 12: 0.0, 13: 3847.4823, 14: 373.7838, 15: 2659.7563,
               16: 48924.2448, 17: 18419.2614, 18: 0.0, 19: 0.0, 20: 35240.1826,
               21: 43829.1667, 22: 18235.6852, 23: 4355.0662, 24: 13327.1025,
               25: 0.0, 26: 0.0, 27: 25681.8318, 28: 1718.1221, 29: 13220.495,
               30: 8414.61}

soma = cont = 0
valores = list()
print('Faturamento do mês:')
for dia, valor in faturamento.items():
    print(f'{dia:<4} {valor:>4}')

for valor in faturamento.values():
    soma += valor
media = soma / len(faturamento.values())

for valor in faturamento.values():
    if valor > 0:
        valores.append(valor)
    if valor > media:
        cont += 1

print('-'*30)
print(f'O menor faturamento ocorrido foi de R${min(valores)}')
print(f'O maior faturamento ocorrido foi de R${max(faturamento.values())}')
print(f'Há um total de {cont} dias em que o valor do faturamento foi maior que a média mensal que é de R${media:.2f}')
