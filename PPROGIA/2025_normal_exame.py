def criar_usernames(emails):
    return sorted(
        map(lambda e: e.split('@')[0].upper(), emails)
    )

def soma_precos(precos):
    return sum(
        map(lambda x: x * 0.85, filter(lambda x: x > 50, precos))
    )

def main():
    pythonemails = [
        'joao.silva@empresa.pt',
        'ana.costa@empresa.pt',
        'pedro.santos@empresa.pt',
        'maria.ferreira@empresa.pt',
        'carlos.mendes@empresa.pt'
    ]

    print('## Exercício 1 ##')
    result = criar_usernames(pythonemails)
    print(result)

    precos = [25.50, 80.00, 45.00, 120.00, 35.00, 55.00, 60.00]
    print('## Exercício 2 ##')
    result = soma_precos(precos)
    print(result)
    
if __name__ == "__main__":
    main()
