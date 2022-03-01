from time import sleep


def linha(s):
    print(f"{f'{s}' * 60}")


dados = list()
ficha = list()
while True:
    nome = input('Aluno: ')
    media = float(input('Média: '))
    resp = ' '
    dados.append(nome)
    dados.append(media)
    ficha.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
linha('=')
print(f'{"Nº":<22}{"Aluno":20}{"Média":>4}')
linha('-')
for i, a in enumerate(ficha):
    print(f'{i:<22}{a[0]:20}{a[1]:>4.1f}')
for i in range(0, len(ficha)):
    if ficha[i][1] >= 7:
        ficha[i].append('Aprovado')
    if 7 > ficha[i][1] >= 5:
        ficha[i].append('Recuperação')
    if ficha[i][1] < 5:
        ficha[i].append('Reprovado')
linha('=')
i = int(input('\nDigite o número do aluno para ver o boletim: '))

print('gerando boletim ', end=''), sleep(1), print('.', end=''), sleep(2), print('.', end='')
sleep(2)
print('.')
sleep(1)
linha('=')
print(f'{"FICHA DO ALUNO":^60}')
linha('=')
print(f'Nome do Aluno: {ficha[i][0]}')
print(f'Média de {ficha[i][0]} = {ficha[i][1]}')
print(f'Situção de {ficha[i][0]} = {ficha[i][2]}')
linha('=')
