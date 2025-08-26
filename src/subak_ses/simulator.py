import numpy as np
from typing import Dict, Sequence, Optional, Union
from scipy.integrate import solve_ivp

from .model.system import rhs, compute_harvest  # <-- need a function to compute H(t)
from .config import InitialState, Parameters


def run_simulation(
    state: Union[InitialState, Sequence[float]],
    params: Union[Parameters, Dict],
    span: Sequence[float],
    t_eval: Optional[Sequence[float]] = None,
) -> Dict[str, np.ndarray]:
    r"""
    Run simulation of Subak SES dynamics, including harvest H(t).

    Args:
        state: Initial state, either `InitialState` dataclass or raw array [W, P, T, G].
        params: Parameters, either `Parameters` dataclass or dict.
        span: Time interval (t0, tf).
        t_eval: Optional time points for evaluation.

    Returns:
        dict:
            - "t": time points
            - "y": state trajectories, shape = (n_states, n_times)
            - "H": harvest over time
    """
    if isinstance(state, InitialState):
        y0 = state.as_array()
    else:
        y0 = np.array(state, dtype=float)

    if isinstance(params, Parameters):
        param_dict = params.as_dict()
    else:
        param_dict = params

    if t_eval is None:
        t_eval = np.linspace(span[0], span[1], 500)

    sol = solve_ivp(
        fun=lambda t, y: rhs(t, y, param_dict),
        t_span=span,
        y0=y0,
        t_eval=t_eval,
        vectorized=False,
    )

    if not sol.success:
        raise RuntimeError("Simulation failed: " + sol.message)

    # Compute harvest H(t) from the state
    H = compute_harvest(sol.y, param_dict)  # shape = (n_times,)

    return {
        "t": sol.t,
        "y": sol.y,  # shape (n_states, n_times)
        "H": H,  # shape (n_times,)
    }
