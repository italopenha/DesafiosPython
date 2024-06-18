"""Este programa tem uma tupla com várias palavras. Ele mostra, para cada
palavra contida na tupla, quais são as suas vogais."""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'Na palavra {p.upper()} temos', end=' ')
    for i in range(0, len(p)):
        if p[i] == 'a' or p[i] == 'e' or p[i] == 'i' or p[i] == 'o' or p[i] == 'u':
            print(p[i], end=' ')
    print()
