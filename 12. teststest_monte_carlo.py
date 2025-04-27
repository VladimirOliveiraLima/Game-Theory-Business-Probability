from src.montecarlo_game.simulator import GameSimulator
from src.montecarlo_game.payoff_matrix import get_estratégia_juridica_matrix
from src.montecarlo_game.monte_carlo import monte_carlo_simulation

def test_simulation_runs():
    simulator = GameSimulator(get_estratégia_juridica_matrix())
    results = monte_carlo_simulation(simulator, iterations=10)
    assert len(results) == 10
