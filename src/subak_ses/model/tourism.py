from typing import Dict


def tourism(T: float, G: float, params: Dict) -> float:
    r"""
    Tourism demand dynamics.

    Equation:
        .. math::

            \frac{dT}{dt} =
                k_t \Big( D_{ext} - \beta_T G T - T \Big)
    """
    return params["k_t"] * (params["D_ext"] - params["beta_T"] * G * T - T)
