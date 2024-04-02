# Este programa lê o primeiro termo e a razão de uma Progressão Aritmética.
# No final, mostra os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1

print(primeiro_termo)
outros_termos = primeiro_termo

while contador < 10:
    outros_termos += razao
    print(outros_termos)
    contador += 1


