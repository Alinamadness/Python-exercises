from fibonacci import fibonacci_loop
# from vec_insert_zero import insert_zeros

# Task1 - element of Fibonacci sequence
print('Input the integer positive number (or zero) - the index of Fibonacci sequence')
n = input()
print(f'The {n}th element of Fibonacci sequence is equal to {fibonacci_loop(n)}')

# Task2 - insert zero into list of numbers
# Fill the list v with integer numbers
v = [1, 2, 3]
print(f'The vector {v} with inserted zeros is equal to {insert_zeros(v)}')
