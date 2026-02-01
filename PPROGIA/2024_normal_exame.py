# Exame época de normal – 15/11/2024

def func_aprovados(pessoas):
    return list(
        map(
            lambda x: 2024 - x['ano_nascimento'], filter(lambda x: x['aprovado'], pessoas)
        )
    )

def calcular_total_com_aumento(precos):
    return sum(
        map(lambda x: x*1.1, filter(lambda x: x*1.1 <= 50, precos))
    )

def main():
    pessoas = [
        {'nome': 'Ana', 'ano_nascimento': 1995, 'aprovado': True},
        {'nome': 'Bruno', 'ano_nascimento': 2000, 'aprovado': False},
        {'nome': 'Carla', 'ano_nascimento': 1985, 'aprovado': True},
        {'nome': 'Daniel', 'ano_nascimento': 1990, 'aprovado': True},
    ]

    print('## Exercício 1 ##')
    result = func_aprovados(pessoas)
    print('Idades Pessoas Aprovadas: ', result)

    print('## Exercício 2 ##')
    precos = [20.0, 50.0, 100.0, 30.0]
    result = calcular_total_com_aumento(precos)
    print('Filtro de aumento de preços: ', result)

if __name__ == "__main__":
    main()
