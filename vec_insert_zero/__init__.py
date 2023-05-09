import numpy as np

def insert_zeros(v):
    try:
        a = np.array(v)
        if len(a) == 0:
            raise ValueError('Length of vector must be non-zero')
        if any(a == 0):
            raise ValueError('Elements must be non-zero')
        positions_to_insert = range(1, len(a))
        a = np.insert(a, positions_to_insert, 0)
        return list(a)
    except (ValueError, TypeError):
        raise ValueError('Vector must be a list with integers')