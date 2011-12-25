"""
Helper tools

"""

def set_value_rec(branch, keys, value):
    """
    Recursivelly traverse `branch` until the end of `keys` is
    reached and set the value.

    :Parameters:
      - `branch`: dictionary
      - `keys`: a list of keys that define path to the key to be set
      - `value`: a value to store

    """
    if len(keys) == 1:
        branch[keys[0]] = value
        return branch
    key = keys.pop(0)
    res = set_value_rec(branch.setdefault(key, {}), keys,
                                value)
    branch[key].update(res)
    return branch

