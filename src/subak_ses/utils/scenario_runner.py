import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subak_ses.simulator import run_simulation
from subak_ses.config import default_state
from .analysis import summary_stats

sns.set_theme(style="whitegrid", context="talk")


def run_scenarios(scenarios: dict, span=(0, 120)) -> dict:
    """Run multiple scenarios and return results as DataFrames, including H(t)."""
    results = {}
    for name, params in scenarios.items():
        sim = run_simulation(default_state, params, span=span)
        df = pd.DataFrame(
            sim["y"].T, columns=["Water", "Rice", "Tourism", "Governance"]
        )
        df["t"] = sim["t"]
        df["Harvest"] = sim["H"]
        results[name] = df
    return results


def plot_scenarios(results: dict):
    """Compare scenarios: vertical layout, one variable per subplot including Harvest."""
    variables = ["Water", "Rice", "Tourism", "Governance", "Harvest"]
    colors = sns.color_palette("tab10", n_colors=len(results))

    fig, axes = plt.subplots(len(variables), 1, figsize=(10, 16), sharex=True)

    for ax, var in zip(axes, variables):
        for (name, df), color in zip(results.items(), colors):
            ax.plot(df["t"], df[var], label=name, color=color, linewidth=2)
        ax.set_title(var, fontsize=14, fontweight="bold")
        ax.set_ylabel(var)
        ax.legend()

    axes[-1].set_xlabel("Time (months)")
    plt.suptitle("Scenario Comparison", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()


def plot_single_scenario(name: str, df: pd.DataFrame):
    """Plot one scenario: vertical layout including Harvest."""
    variables = ["Water", "Rice", "Tourism", "Governance", "Harvest"]
    fig, axes = plt.subplots(len(variables), 1, figsize=(10, 16), sharex=True)

    for ax, var in zip(axes, variables):
        sns.lineplot(x="t", y=var, data=df, ax=ax, color="C0", linewidth=2.5)
        ax.set_title(var, fontsize=14, fontweight="bold")
        ax.set_ylabel(var)

    axes[-1].set_xlabel("Time (months)")
    plt.suptitle(f"Scenario: {name}", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()


def report_scenarios(results: dict):
    """For each scenario: show vertical subplot and summary stats including Harvest."""
    for name, df in results.items():
        plot_single_scenario(name, df)
        print(f"\n{name} scenario analysis:")
        print(
            summary_stats(
                {
                    "t": df["t"].values,
                    "y": df[
                        ["Water", "Rice", "Tourism", "Governance", "Harvest"]
                    ].values.T,
                }
            )
        )
