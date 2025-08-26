from typing import Dict


def agriculture(W: float, P: float, params: Dict) -> float:
    r"""
    Agriculture (rice dynamics).

    Equation:
        .. math::

            \frac{dP}{dt} =
                r_p P \left( 1 - \frac{P}{K_p} \right)
                \frac{W}{W + K_w}
                - \delta_p P
    """
    fW = W / (W + params["K_w"])
    return params["r_p"] * P * (1 - P / params["K_p"]) * fW - params["delta_p"] * P
