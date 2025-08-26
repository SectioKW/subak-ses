# subak_ses/models/system.py
import numpy as np
from typing import Tuple, Dict, Callable
from .hydrology import hydrology
from .agriculture import agriculture
from .tourism import tourism
from .governance import governance
from .harvest import compute_harvest


def rhs(
    t: float,
    y: np.ndarray,
    params: Dict,
    Rin_func: Callable[[float], float],
    D_ext_func: Callable[[float], float],
) -> np.ndarray:
    """
    Full system RHS. y order: [W, P, T, G]
    """
    W, P, T, G = float(y[0]), float(y[1]), float(y[2]), float(y[3])

    dW = hydrology(t, W, P, T, params, Rin_func)
    dP = agriculture(W, P, params)
    dT = tourism(T, D_ext_func(t), G, params)
    dG = governance(W, P, T, G, params)

    return np.array([dW, dP, dT, dG], dtype=float)


# make compute_harvest available from this module too
__all__ = ["rhs", "compute_harvest"]
