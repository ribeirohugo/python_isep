# Exame – 18/11/2022

from functools import reduce

def func_3a(numeros):
    return reduce(
        lambda x, y: str(x)+'|'+str(y), filter(lambda x: x % 2 == 0, numeros)
    )

def func_3b(val_list, val_int):
    return sum(
        map(lambda x: x, filter(lambda x: x % val_int == 0, val_list))
    )

def main():
    print('## Exercício 1 ##')
    numeros = [1,2,4,55,22]
    result = func_3a(numeros)
    print('Números Pares: ', result)

    print('## Exercício 2 ##')
    numeros = [1,2,4,55,22,9,6]
    result = func_3b(numeros, 2)
    print('Números múltilos: ', result)

if __name__ == "__main__":
    main()
