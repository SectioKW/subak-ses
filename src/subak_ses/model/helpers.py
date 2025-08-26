# subak_ses/models/helpers.py
from typing import Callable, Dict
import numpy as np


def f_w(W: float, K_w: float) -> float:
    """Michaelis–Menten saturating function f(W) = W/(W + K_w)."""
    W_eff = max(W, 0.0)
    if K_w <= 0.0:
        return 1.0 if W_eff > 0 else 0.0
    return W_eff / (W_eff + K_w)


def S_crisis(W: float, params: Dict) -> float:
    """
    Crisis shock; returns s_crisis when W < W_threshold else 0.
    params expected to contain 'W_threshold' and 's_crisis'.
    """
    return params.get("s_crisis", 0.0) if W < params.get("W_threshold", 0.0) else 0.0


# --- convenient exogenous drivers ---
def seasonal_rain(params: Dict) -> Callable[[float], float]:
    """
    Build a seasonal rainfall function using parameters:
    'rain_mean', 'rain_amp', 'rain_period'
    """
    mean = params.get("rain_mean", 0.0)
    amp = params.get("rain_amp", 0.0)
    period = params.get("rain_period", 1.0)

    def Rin(t: float) -> float:
        return mean + amp * np.sin(2 * np.pi * (t / period))

    return Rin


def constant_demand(value: float) -> Callable[[float], float]:
    """Return a constant demand function D_ext(t) = value."""
    return lambda t: float(value)


def pulsed_demand(
    base: float, pulse_value: float, start: float, end: float
) -> Callable[[float], float]:
    """Return a demand that is base normally and pulse_value between start and end."""

    def D_ext(t: float) -> float:
        return pulse_value if (t >= start and t <= end) else base

    return D_ext
