# src/subak_ses/utils/visualization.py
import matplotlib.pyplot as plt


def plot_simulation(result, labels=None, title="Subak SES Dynamics"):
    """
    Plot state trajectories from simulation results.

    Args:
        result (dict): Output from `run_simulation`, with keys "t" and "y".
        labels (list[str], optional): Names for each state variable.
        title (str): Figure title.
    """
    t = result["t"]
    y = result["y"]

    if labels is None:
        labels = ["Water", "Rice", "Tourism", "Governance"]

    plt.figure(figsize=(10, 6))
    for i in range(y.shape[0]):
        plt.plot(t, y[i], label=labels[i])
    plt.xlabel("Time")
    plt.ylabel("State Value")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
