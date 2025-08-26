import numpy as np
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class InitialState:
    """Initial state variables [W, P, T, G]."""

    water: float = 30.0  # Water storage (m^3)
    rice: float = 30.0  # Rice population/area
    tourism: float = 20.0  # Tourism demand
    governance: float = 0.5  # Governance intensity (0..1)

    def as_array(self) -> np.ndarray:
        """Return state as numpy array [W, P, T, G]."""
        return np.array(
            [self.water, self.rice, self.tourism, self.governance], dtype=float
        )


@dataclass(frozen=True)
class Parameters:
    """Model parameters for Subak SES dynamics."""

    # Hydrology
    lambda_W: float = 0.08  # Evaporation rate
    K_w: float = 40.0  # Water saturation half-constant
    rain_mean: float = 40.0  # Mean rainfall inflow
    rain_amp: float = 15.0  # Seasonal amplitude
    rain_period: float = 12.0  # Period of rainfall oscillation (months)

    # Agriculture
    alpha_p: float = 0.04  # Water demand coefficient (rice)
    r_p: float = 0.12  # Rice growth rate
    K_p: float = 80.0  # Carrying capacity (rice)
    delta_p: float = 0.03  # Rice decay/mortality

    # Tourism
    alpha_t: float = 0.02  # Water demand coefficient (tourism)
    k_t: float = 0.07  # Adjustment rate for tourism demand
    D_ext: float = 60.0  # External tourism demand
    beta_T: float = 0.6  # Governance effect on tourism demand

    # Governance
    rho: float = 0.08  # Governance adjustment rate
    gamma1: float = 0.12  # Shock responsiveness
    gamma2: float = 0.08  # Rice-target responsiveness
    decay: float = 0.03  # Governance decay
    P_target: float = 50.0  # Target rice population

    def as_dict(self) -> dict:
        return asdict(self)


default_state = InitialState()
default_params = Parameters()
