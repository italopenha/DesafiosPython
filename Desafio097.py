"""Este programa tem uma função chamada escreva(), que recebe um texto qualquer como
parâmetro e mostra uma mensagem com tamanho adaptável."""

def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt}')
    print('~' * (len(txt) + 2))

escreva("Ítalo Penha")
escreva("Curso de Python no YouTube")
escreva("CeV")