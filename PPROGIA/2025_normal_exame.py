def criar_usernames(emails):
    return sorted(
        map(lambda e: e.split('@')[0].upper(), emails)
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

if __name__ == "__main__":
    main()
