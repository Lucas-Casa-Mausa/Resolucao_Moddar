"""Aqui na Moodar, estamos precisando organizar algumas informações. Temos um JSON (enviado por email) das consultas realizadas em 2024 no Japão, de uma empresa parceira nossa. Para cada consulta, temos a data de realização, o paciente, o terapeuta e o plano daquele paciente. Todo ano, realizamos a retrospectiva daquele ano. Essa retrospectiva possui: 

1- Qual foi o plano mais contratado

2- Qual o terapeuta que possuiu mais consultas

3- Quantas consultas aconteceram em cada mês

OBS: o sistema salva a data no formato utilizado do japão, garanta que o formato apresentado, de acordo com o mês, está de acordo com o brasileiro!

Objetivo: Avaliar a capacidade de agrupar, resumir e manipular dados, lidando com objetos, arrays e datas.
"""

import json

with open('sessoes_terapia_2024_japan (1).json', 'r', encoding='utf-8') as f:
    consultas = json.load(f)


contagem_planos = {}
for consulta in consultas:
    plano = consulta['plano']
    contagem_planos[plano] = contagem_planos.get(plano, 0) + 1
plano_mais_contratado = max(contagem_planos.items(), key=lambda x: x[1])


contagem_terapeutas = {}
for consulta in consultas:
    terapeuta = consulta['terapeuta'].strip()  # Remove espaços extras
    contagem_terapeutas[terapeuta] = contagem_terapeutas.get(terapeuta, 0) + 1
terapeuta_mais_consultas = max(contagem_terapeutas.items(), key=lambda x: x[1])


meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril',
    'Maio', 'Junho', 'Julho', 'Agosto',
    'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]
contagem_meses = {}
for consulta in consultas:
    data_str = consulta['data'].split()[0]
    ano, mes, _ = data_str.split('/')
    nome_mes = meses[int(mes) - 1]
    chave = f"{nome_mes} {ano}"
    contagem_meses[chave] = contagem_meses.get(chave, 0) + 1


print("1. Plano mais contratado:")
print(f"   {plano_mais_contratado[0]} com {plano_mais_contratado[1]} consultas\n")

print("2. Terapeuta com mais consultas:")
print(f"   {terapeuta_mais_consultas[0]} com {terapeuta_mais_consultas[1]} consultas\n")

print("3. Consultas por mês:")
print("| Mês           | Quantidade de Consultas |")
print("|---------------|-------------------------|")
for mes in meses:
    chave = f"{mes} 2024"
    qtd = contagem_meses.get(chave, 0)
    print(f"| {chave.ljust(13)} | {str(qtd).center(23)} |")