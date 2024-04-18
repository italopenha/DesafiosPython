# Este programa lê o primeiro termo e a razão de uma Progressão Aritmética.
# No final, mostra os 10 primeiros termos dessa progressão e pergunta ao usuário
# se ele deseja ver mais termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1

print(primeiro_termo, end=' ')
outros_termos = primeiro_termo

while contador < 10:
    outros_termos += razao
    print(outros_termos, end=' ')
    contador += 1

opcao = int
print('\nEsses são os 10 primeiros termos dessa Progressão Aritmética.')

while opcao != 0:
    opcao = int(input('\nDeseja ver mais termos? Se sim, digite a quantidade ou digite [0] para sair. '))

    if opcao != 0:
        opcao += contador

        while contador < opcao:
            outros_termos += razao
            print(outros_termos, end=' ')
            contador += 1

print(f'Progressão finalizada com {contador} termos mostrados.')
