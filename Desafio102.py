def fatorial(n, show=False):
    """
    Calcula o fatorial de um número inteiro
    :param n: O númeoro a ser calculado
    :param show: (opcional) Mostrar ou não a conta do fatorial
    :return: O valor do fatorial de um número n
    """
    f = 1
    msg = ''
    nStr = n

    for i in range(1, n + 1):
        f *= i

        if show:
            if n == i:
                msg += f'{nStr} '
            else:
                msg += f'{nStr} X '
            nStr -= 1

    if show:
        return f'{msg.rstrip()} = {f}'
    else:
        return f'{f}'

print(fatorial(5, True))
print(fatorial(5, False))
help(fatorial)


