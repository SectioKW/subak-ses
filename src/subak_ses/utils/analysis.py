# src/subak_ses/utils/analysis.py
import numpy as np
import pandas as pd


def summary_stats(result, labels=None) -> pd.DataFrame:
    """
    Compute summary statistics (mean, min, max, std) for each state variable.

    Args:
        result (dict): Simulation result from `run_simulation`.
        labels (list[str], optional): Names of state variables.

    Returns:
        pd.DataFrame: Statistics table (rows = variables, cols = stats).
    """
    y = result["y"]

    if labels is None:
        labels = ["Water", "Rice", "Tourism", "Governance"]

    data = []
    for i, series in enumerate(y):
        stats = {
            "mean": np.mean(series),
            "min": np.min(series),
            "max": np.max(series),
            "std": np.std(series),
        }
        data.append(stats)

    df = pd.DataFrame(data, index=labels)
    return df.round(3)
