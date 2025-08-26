import numpy as np
from typing import Dict


def hydrology(t: float, W: float, P: float, T: float, params: Dict) -> float:
    r"""
    Hydrology dynamics.

    Equation:
        .. math::

            \frac{dW}{dt} = R_{in}(t) - \alpha_p P - \alpha_t T - \lambda_W W

    where:
        - :math:`R_{in}(t) = \bar{R} + A \sin \left( \frac{2 \pi t}{T_{rain}} \right)`
        - :math:`\alpha_p P` = water demand from rice
        - :math:`\alpha_t T` = water demand from tourism
        - :math:`\lambda_W W` = evaporation losses
    """
    Rin = params["rain_mean"] + params["rain_amp"] * np.sin(
        2 * np.pi * t / params["rain_period"]
    )
    Qp = params["alpha_p"] * P
    Qt = params["alpha_t"] * T
    return Rin - Qp - Qt - params["lambda_W"] * W
