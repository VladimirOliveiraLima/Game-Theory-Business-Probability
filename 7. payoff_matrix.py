def get_dilema_prisioneiro_matrix():
    """
    Retorna a matriz de recompensas do Dilema do Prisioneiro:
    A estrutura é:
    payoff_matrix[Ação A][Ação B] = (payoff A, payoff B)
    """
    return {
        "C": {  # Cooperar
            "C": (3, 3),
            "D": (0, 5),
        },
        "D": {  # Trair (Defect)
            "C": (5, 0),
            "D": (1, 1),
        }
    }
