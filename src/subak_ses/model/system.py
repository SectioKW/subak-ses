import numpy as np
from typing import Sequence, Dict

from .hydrology import hydrology
from .agriculture import agriculture
from .tourism import tourism
from .governance import governance


def rhs(t: float, y: Sequence[float], params: Dict) -> np.ndarray:
    r"""
    Full Subak SES system wrapper.

    State variables:
        .. math::

            y = [W, P, T, G]
    """
    W, P, T, G = y

    dWdt = hydrology(t, W, P, T, params)
    dPdt = agriculture(W, P, params)
    dTdt = tourism(T, G, params)
    dGdt = governance(W, P, G, params)

    return np.array([dWdt, dPdt, dTdt, dGdt], dtype=float)


def compute_harvest(y: np.ndarray, params: dict) -> np.ndarray:
    """Compute harvest H(t) based on rice population and parameters."""
    rice = y[1]  # assuming index 1 = Rice
    r_p = params.get("r_p", 0.1)
    K_p = params.get("K_p", 100.0)
    H = r_p * rice * (1 - rice / K_p)
    return H
