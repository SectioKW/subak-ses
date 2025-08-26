# subak_ses/models/agriculture.py
from typing import Dict
from .helpers import f_w


def agriculture(W: float, P: float, params: Dict) -> float:
    """
    Rice productivity dynamics:
      dP/dt = r_p P (1 - P/K_p) f(W) - delta_p P
    """
    fw = f_w(W, params["K_w"])
    return params["r_p"] * P * (1.0 - P / params["K_p"]) * fw - params["delta_p"] * P
