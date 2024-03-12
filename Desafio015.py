# Este programa lê a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado, e calcula o preço a pagar
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

km = float(input('Km percorridos: '))
dias = int(input('Dias pelos quais o carro foi alugado: '))

total = dias * 60 + km * 0.15

print(f'O total a pagar é de R$ {total:.2f}')