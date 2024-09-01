import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)


faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]


menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)


print("Menor valor de faturamento: R${menor_faturamento}")
print("Maior valor de faturamento: R${maior_faturamento}")
print("Número de dias com faturamento acima da média: {dias_acima_da_media}")
