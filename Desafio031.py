# Este programa lê uma distância em Km de uma viagem e calcula o preço da passagem.

distancia = float(input('Digite a distância da viagem em Km: '))

passagem = 0.0

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print(f'A sua passagem vai custar R$ {passagem:.2f}')