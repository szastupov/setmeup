import os


def from_env(cls):
    """A class decorator to populate fields from os env"""
    for k, default in vars(cls).items():
        if not k.startswith("_"):
            vtype = type(default)
            val = os.environ.get(k.upper(), default)

            if vtype == bool and val != default:
                val = False if val == "0" else True

            setattr(cls, k, vtype(val))
    return cls
