9. utils.py

def summarize_results(results):
    payoff_a = sum([r["payoff_a"] for r in results])
    payoff_b = sum([r["payoff_b"] for r in results])
    return {
        "media_payoff_a": payoff_a / len(results),
        "media_payoff_b": payoff_b / len(results)
    }
