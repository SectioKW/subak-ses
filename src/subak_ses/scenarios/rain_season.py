# scenarios/drought.py
"""
Rain season scenario: 75% increase in mean rainfall.
"""

from subak_ses.config import Parameters

rain_season_params = Parameters(rain_mean=Parameters().rain_mean * 1.75)
