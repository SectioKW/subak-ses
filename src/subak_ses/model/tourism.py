# subak_ses/models/tourism.py
from typing import Dict, Callable


def tourism(T: float, D_ext: float, G: float, params: Dict) -> float:
    """
    Tourism dynamics.

    We use the formulation:
        dT/dt = alpha_T * D_ext(t) - beta_T * G * T

    - alpha_T scales how external demand translates into realized tourism growth.
    - beta_T * G * T is governance-imposed damping proportional to current T.
    """
    return params["alpha_T"] * float(D_ext) - params["beta_T"] * G * T
