from src.montecarlo_game.simulator import GameSimulator
from src.montecarlo_game.payoff_matrix import get_estratégia_juridica_matrix

def test_play_returns_dict():
    matrix = get_dilema_prisioneiro_matrix()
    sim = GameSimulator(matrix)
    result = sim.play(lambda: "C", lambda: "D")
    assert "payoff_a" in result and "payoff_b" in result
