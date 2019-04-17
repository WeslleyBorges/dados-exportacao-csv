'''import csv, io
with open('levantamento_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #cabecalho = True
    #next(csv_reader)
    distrito = {}
    distrito['descricao_distrito'] = []
    for row in csv_reader:
        distrito['descricao_distrito'].append(row[4])

print(distrito['descricao_distrito'])'''
dicionario = {}
array_dicionarios = []

dicionario['nome'] = 'Weslley'
dicionario['idade'] = 22

array_dicionarios.append(dicionario)

dicionario['nome'] = 'Beatriz'
dicionario['idade'] = 21

array_dicionarios.append(dicionario)

print(array_dicionarios)