# subak_ses/models/hydrology.py
from typing import Dict, Callable
from .helpers import f_w


def Q_p(W: float, P: float, params: Dict) -> float:
    """
    Agricultural water consumption.
    Chosen form: proportional to rice P, scaled by availability via f_w.
    Q_p = q_p_coeff * P * f(W)
    """
    return params["q_p_coeff"] * P * f_w(W, params["K_w"])


def Q_t(T: float, params: Dict) -> float:
    """Tourism water consumption: Q_t = q_t_coeff * T"""
    return params["q_t_coeff"] * T


def hydrology(
    t: float,
    W: float,
    P: float,
    T: float,
    params: Dict,
    Rin_func: Callable[[float], float],
) -> float:
    """
    Water dynamics:
        dW/dt = Rin(t) - Q_p(W,P) - Q_t(T) - lambda_w * W
    """
    Rin = Rin_func(t)
    return Rin - Q_p(W, P, params) - Q_t(T, params) - params["lambda_w"] * W
