# subak_ses/models/governance.py
from typing import Dict
from .helpers import S_crisis


def governance(W: float, P: float, T: float, G: float, params: Dict) -> float:
    """
    Governance dynamics:

        dG/dt = rho * ( gamma1 * W/W_ref + gamma2 * P/K_p - gamma3 * T/T_ref - G )
                + S_crisis(W)

    where S_crisis(W) is a discrete shock when W drops below threshold.
    """
    W_ref = params.get("W_ref", 1.0)
    T_ref = params.get("T_ref", 1.0)

    term = (
        params["gamma1"] * (W / W_ref if W_ref != 0 else 0.0)
        + params["gamma2"] * (P / params["K_p"] if params["K_p"] != 0 else 0.0)
        - params["gamma3"] * (T / T_ref if T_ref != 0 else 0.0)
    )

    dG = params["rho"] * (term - G) + S_crisis(W, params)

    # ---- Option 1: Hard clamp on [0,1] ----
    if G >= 1.0 and dG > 0:
        dG = 0.0
    elif G <= 0.0 and dG < 0:
        dG = 0.0

    return dG
