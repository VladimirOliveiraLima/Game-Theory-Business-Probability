from src.montecarlo_game.payoff_matrix import get_estratégia_juridica_matrix

def test_matrix_structure():
    matrix = get_dilema_prisioneiro_matrix()
    assert "C" in matrix and "D" in matrix
    assert isinstance(matrix["C"]["C"], tuple)
