# Exame época Normal – 14/09/2025 - Grupo 3
from cpmpy import *

def main():
    print("## A - Identificar Variáveis ##")
    VA = intvar(0, 12, name="VA")
    VB = intvar(0, 12, name="VB")
    VC = intvar(0, 12, name="VC")
    VD = intvar(0, 12, name="VD")
    VE = intvar(0, 12, name="VE")

    print("## B - Restrições Temporais ##")
    dur = {
        VA: 2,
        VB: 3,
        VC: 4,
        VD: 4,
        VE: 2
    }

    model = Model()

    model += VB >= VA + dur[VA] # VB após VA
    model += VD >= VC + dur[VC] # VD após VC
    model += VE >= VB + dur[VB] # VE após VB

    print("## C - Todas as operações dentro de 12 horas ##")
    for v in [VA, VB, VC, VD, VE]:
        model += v + dur[v] <= 12

    print(" D - Restrições de Recursos (Tripulantes)")
    crew = {
        VA: 3,
        VB: 3,
        VC: 2,
        VD: 2,
        VE: 3
    }

    model += Cumulative(
        start=[VA, VB, VC, VD, VE],
        duration=[dur[VA], dur[VB], dur[VC], dur[VD], dur[VE]],
        demand=[crew[VA], crew[VB], crew[VC], crew[VD], crew[VE]],
        capacity=6
    )

    print("## SOLVE MODEL ##")
    if model.solve():
        print("Solução encontrada:\n")
        print(f"VA começa em {VA.value()} h")
        print(f"VB começa em {VB.value()} h")
        print(f"VC começa em {VC.value()} h")
        print(f"VD começa em {VD.value()} h")
        print(f"VE começa em {VE.value()} h")
    else:
        print("Não existe solução viável")
    
if __name__ == "__main__":
    main()
