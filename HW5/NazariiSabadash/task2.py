def fibonacci(n):
    sequence = [0, 1]
    current = 0
    while current < n:
        current = sum(sequence[-2:])
        sequence.append(current)
    print(sequence)


fibonacci(89)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibonacci(610)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
