"""MongoDB time series in Python."""

__version_tuple__ = (0, 0, 1)

def get_version_string():
    """
    Format version tuple as a string.

    """
    return '.'.join([str(x) for x in __version_tuple__])

__version__ = get_version_string()
