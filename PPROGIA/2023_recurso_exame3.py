# Exame época de recurso – 01/02/2024
from cpmpy import *

def main():
    M1 = intvar(0, 60, name="armario")
    M2 = intvar(0, 60, name="cadeiras")
    M3 = intvar(0, 60, name="cama")
    M4 = intvar(0, 60, name="mesa")

    dur = {M1: 20, M2: 8, M3: 15, M4: 12}

    model = Model()
    model += M2 >= M4 + dur[M4]

    for n in [M1, M2, M3, M4]:
        model += n + dur[n] <= 60

    homens = {M1: 3, M2: 2, M3: 3, M4: 2}

    model += Cumulative(
        start=[M1, M2, M3, M4],
        duration=[dur[M1], dur[M2], dur[M3], dur[M4]],
        demand=[homens[M1], homens[M2], homens[M3], homens[M4]],
        capacity=4
    )

    print("## SOLVE MODEL ##")
    if model.solve():
        print("Solução encontrada:\n")
        print(f"M1 começa em {M1.value()} min")
        print(f"M2 começa em {M2.value()} min")
        print(f"M3 começa em {M3.value()} min")
        print(f"M4 começa em {M4.value()} min")
    else:
        print("Não existe solução viável")

if __name__ == "__main__":
    main()
