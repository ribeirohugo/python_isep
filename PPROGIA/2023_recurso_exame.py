# Exame época de recurso – 01/02/2024

def findPythonSentences(frases):
    return list(
        map(
            lambda x: x.lower(), filter(lambda x: 'python' in x.lower(), frases)
        )
    )

def findMaxPair(numeros):
    return max(
        map(
            lambda x: x, filter(lambda x: x % 2 == 0, numeros)
        )
    )

def main():
    frases = [
        "Python é uma linguagem poderosa e versátil.",
        "Programação funcional oferece um paradigma diferente.",
        "A inteligência artificial está a transformar o mundo.",
        "List comprehensions são úteis em Python.",
        "Map, filter e reduce são funções de primeira ordem."
    ]

    print('## Exercício 1 ##')
    result = findPythonSentences(frases)
    print('Frases que contêm Python: ', result)

    print('## Exercício 2 ##')
    numeros = [1, 2, 7, 12, 5, 22, 56, 53, 54, 33, 57, 63]
    result = findMaxPair(numeros)
    print('Máximo Número Par: ', result)

if __name__ == "__main__":
    main()
