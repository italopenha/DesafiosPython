textoInicial = 'SISTEMA DE AJUDA PyHELP'
textoFinal = 'ATÉ LOGO!'

def imprimirTextoPersonalizado(texto, corFundo = 'reset'):
    print(f"{'~' * (len(texto) + 4)}")
    print(f'  {texto}')
    print(f"{'~' * (len(texto) + 4)}")

while True:
    imprimirTextoPersonalizado(textoInicial)

    funcaoBiblioteca = input(f'Função ou Biblioteca: ')

    textoAcessando = f'Acessando o manual do comando "{funcaoBiblioteca}"'

    if funcaoBiblioteca.lower() == 'fim':
        imprimirTextoPersonalizado(textoFinal, corFundo='vermelho')
        break
    else:
        imprimirTextoPersonalizado(textoAcessando)
        help(funcaoBiblioteca)
        continue

