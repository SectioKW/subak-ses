import numpy as np


def compute_harvest(y, params):
    """
    Compute harvest H(t) over the trajectory y(t).
    y: ndarray with shape (n_vars, n_timepoints)
    params: dict-like with parameter values
    """
    W = y[0]  # Water trajectory
    R = y[1]  # Rice trajectory

    # Clamp water at zero elementwise
    W_eff = np.maximum(W, 0.0)

    # Parameters
    K_w = params.get("K_w", 1.0)  # half-saturation water
    K_r = params.get("K_r", 1.0)  # half-saturation rice
    alpha = params.get("alpha", 1.0)  # harvest efficiency

    # Saturating functions (bounded between 0–1)
    W_frac = W_eff / (W_eff + K_w)
    R_frac = R / (R + K_r)

    # Harvest (vectorized)
    H = alpha * W_frac * R_frac

    return H
