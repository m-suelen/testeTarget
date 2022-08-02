faturamento = {'SP': 67.83643, 'RJ': 36.67866, 'MG': 29.22988,
               'ES': 27.16548, 'Outros': 19.84953}

soma = 0
for valor in faturamento.values():
    soma += valor
for est, valor in faturamento.items():
    perc = (valor / soma) * 100
    print(f'{est} = {perc:.2f}%')
