import numpy as np
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class InitialState:
    """Initial state variables [W, P, T, G]."""

    water: float = 30.0  # Water storage
    rice: float = 30.0  # Rice productivity proxy
    tourism: float = 20.0  # Tourism scale
    governance: float = 0.2  # Governance index (0–1)

    def as_array(self) -> np.ndarray:
        return np.array(
            [self.water, self.rice, self.tourism, self.governance], dtype=float
        )


@dataclass(frozen=True)
class Parameters:
    """Unified parameter set for Subak SES model."""

    # --- Water (3.2.1) ---
    lambda_w: float = 0.08  # Evaporation / leakage
    q_p_coeff: float = 0.6  # Water demand coefficient (agriculture)
    q_t_coeff: float = 0.5  # Water demand coefficient (tourism)

    # Seasonal rainfall forcing
    rain_mean: float = 40.0  # Mean inflow
    rain_amp: float = 15.0  # Amplitude
    rain_period: float = 12.0  # Period (months)

    # --- Agriculture (3.2.2) ---
    r_p: float = 0.12  # Growth rate
    K_p: float = 80.0  # Carrying capacity
    K_w: float = 40.0  # Half-saturation constant for water
    delta_p: float = 0.03  # Loss rate

    # --- Tourism (3.2.3) ---
    alpha_T: float = 0.05  # Sensitivity to external demand
    beta_T: float = 0.6  # Governance restriction strength

    # --- Governance (3.2.4) ---
    rho: float = 0.2  # Adaptation rate
    gamma1: float = 0.12  # Weight of W
    gamma2: float = 0.2  # Weight of P
    gamma3: float = 0.10  # Weight of T
    W_ref: float = 40.0  # Reference water
    T_ref: float = 50.0  # Reference tourism

    s_crisis: float = 0.2  # Shock magnitude
    W_threshold: float = 15.0  # Crisis threshold

    # --- Output (3.2.5) ---
    n: float = 1.0  # Harvest conversion coefficient

    def as_dict(self) -> dict:
        return asdict(self)


default_state = InitialState()
default_params = Parameters()
