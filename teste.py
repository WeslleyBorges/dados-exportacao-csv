import csv
with open('levantamento_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True
    for row in csv_reader:
        '''if cabecalho:
            print(f'Nomes das colunas: {", ".join(row)}')
            cabecalho = False
        else:
            print(f'{", ".join(row)}')'''
        print(row)