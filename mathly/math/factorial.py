def factorial(x):
    """
    Returns x factorial.
    """
    # TODO(aaronhma): Instead of recursion, replace this:
    if x == 1: # Base case
        return x
    else: # Recursion
        return x * factorial(x - 1)