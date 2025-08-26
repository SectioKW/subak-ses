# subak_ses/simulation.py
import numpy as np
from typing import Dict, Sequence, Optional, Union, Callable
from scipy.integrate import solve_ivp

from .model.system import rhs, compute_harvest
from .config import InitialState, Parameters
from .model.helpers import seasonal_rain, constant_demand


def run_simulation(
    state: Union[InitialState, Sequence[float]],
    params: Union[Parameters, Dict],
    span: Sequence[float],
    Rin_func: Optional[Callable[[float], float]] = None,
    D_ext_func: Optional[Callable[[float], float]] = None,
    t_eval: Optional[Sequence[float]] = None,
) -> Dict[str, np.ndarray]:
    """
    Run simulation and return {'t', 'y', 'H'}.

    - state: InitialState dataclass or raw array [W, P, T, G]
    - params: Parameters dataclass or plain dict
    - Rin_func: rainfall forcing function. If None, uses seasonal_rain(params)
    - D_ext_func: external tourism demand function. If None, uses constant_demand(60.0)
    """
    if isinstance(state, InitialState):
        y0 = state.as_array()
    else:
        y0 = np.array(state, dtype=float)

    if isinstance(params, Parameters):
        param_dict = params.as_dict()
    else:
        param_dict = dict(params)

    if Rin_func is None:
        Rin_func = seasonal_rain(param_dict)

    if D_ext_func is None:
        # default baseline tourism demand constant = 60
        D_ext_func = constant_demand(60.0)

    if t_eval is None:
        t_eval = np.linspace(span[0], span[1], 500)

    sol = solve_ivp(
        fun=lambda t, y: rhs(t, y, param_dict, Rin_func, D_ext_func),
        t_span=(span[0], span[1]),
        y0=y0,
        t_eval=t_eval,
        vectorized=False,
        rtol=1e-6,
        atol=1e-9,
    )

    if not sol.success:
        raise RuntimeError("Simulation failed: " + sol.message)

    H = compute_harvest(sol.y, param_dict)

    return {"t": sol.t, "y": sol.y, "H": H}
