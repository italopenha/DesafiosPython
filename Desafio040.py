# Este programa lê duas notas de um aluno e calcula sua média, mostrando
# uma mensagem final de acordo com a média atingida.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

mediaFinal = 0.4 * nota1 + 0.6 * nota2

if mediaFinal < 5.0:
    print(f'Sua média foi de {mediaFinal:.2f}. Infelizmente você foi reprovado.')
else:
    print(f'Sua média final foi de {mediaFinal:.2f}. Você foi aprovado, parabéns!')