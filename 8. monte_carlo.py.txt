import random

def random_strategy():
    return random.choice(["C", "D"])

def monte_carlo_simulation(simulator, iterations=1000, strategy_type="random"):
    stats = []
    for _ in range(iterations):
        if strategy_type == "random":
            result = simulator.play(random_strategy, random_strategy)
        stats.append(result)
    return stats
