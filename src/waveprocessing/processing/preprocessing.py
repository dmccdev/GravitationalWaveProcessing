import numpy as np
from scipy.signal import detrend


def clean_strain(strain):
    """
    Prepare strain data for analysis.
    """

    # Removes vertical offset and slow linear trend
    strain = detrend(strain)

    return strain
