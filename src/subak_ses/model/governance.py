from typing import Dict


def governance(W: float, P: float, G: float, params: Dict) -> float:
    r"""
    Governance response dynamics.

    Equation:
        .. math::

            \frac{dG}{dt} =
                \rho \Big[
                    \gamma_1 (P_{target} - P) +
                    \gamma_2 W -
                    \delta G
                \Big]
    """
    return params["rho"] * (
        params["gamma1"] * (params["P_target"] - P)
        + params["gamma2"] * W
        - params["decay"] * G
    )
