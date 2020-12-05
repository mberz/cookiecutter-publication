"""Plot utilities and functions
"""

def cm2inch(*tupl):
    """Convert from cm to inches.
    Matplotlib uses inches as default unit.

    Conversion supports tuples as the figsize option for figure.

    """
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)
