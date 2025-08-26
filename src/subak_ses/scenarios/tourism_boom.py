# scenarios/tourism_boom.py
"""
Tourism boom: stronger external demand.
"""

from subak_ses.config import Parameters

tourism_boom_params = Parameters(alpha_T=Parameters().alpha_T * 2)  # e.g. +50%
