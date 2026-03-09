def xor(a: bool, b: bool) -> bool:
    """Returns the exclusive OR of two boolean values."""
    return (a and not b) or (not a and b)