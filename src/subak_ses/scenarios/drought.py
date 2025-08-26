# scenarios/drought.py
"""
Drought scenario: 30% reduction in mean rainfall.
"""

from subak_ses.config import Parameters

drought_params = Parameters(rain_mean=Parameters().rain_mean * 0.3)
