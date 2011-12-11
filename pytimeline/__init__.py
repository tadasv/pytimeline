"""MongoDB time series in Python."""

version_tuple = (0, 1)

def get_version_string():
    return '.'.join(map(str, version_tuple))

version = get_version_string()
