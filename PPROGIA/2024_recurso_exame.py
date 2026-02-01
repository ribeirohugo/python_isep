# Exame época de recurso – 03/02/2025

def alunos_aprovados(notas):
    alunos_aprovados = list (
        map(
            lambda x: x[0], filter(lambda x: x[1]>=10, notas.items())
        )
    )

    notas_arredondadas = list(
        map(lambda x: round(x), notas.values())
    )

    print('Alunos Aprovados: ', alunos_aprovados)
    print('Notas Arredondadas: ', notas_arredondadas)

def alunos_aprovados_2(notas):
    alunos_aprovados = list (
        map(lambda nome: nome, filter(lambda nome: notas[nome]>=10, notas))
    )

    notas_arredondadas = list(
        map(lambda valor: round(notas[valor]), notas)
    )

    print('Alunos Aprovados: ', alunos_aprovados)
    print('Notas Arredondadas: ', notas_arredondadas)

def produto_impares(numeros):
    impares = list(
        map(lambda x: x, filter(lambda x: x  % 2 != 0, numeros))
    )

    produto = 1
    for n in impares:
        produto *= n

    return produto

def main():
    notas = {
        "Ana": 14.6,
        "Bruno": 9.2,
        "Carla": 12.8,
        "Daniel": 15.1,
        "Eduardo": 7.5
    }

    print('## Exercício 1 ##')
    result = alunos_aprovados(notas)

    print('## Exercício 2 ##')
    numeros = [3, 8, 5, 10, 7, 2]
    result = produto_impares(numeros)
    print('Produto Números Ímpares: ', result)

    print('## Exercício 2 ##')
    numeros = [2, 4, 6]
    result = produto_impares(numeros)
    print('Produto Números Ímpares: ', result)

if __name__ == "__main__":
    main()
