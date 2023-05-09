def fibonacci_loop(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError('Number must be greater or equal to zero')
        a1, a2 = 1, 1
        if n in (0, 1):
            return n
        for i in range(2, n):
            a1, a2 = a2 + a1, a1
        return a1
    except (ValueError, TypeError):
        raise ValueError('Number must be integer')
