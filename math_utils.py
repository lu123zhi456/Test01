def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci sequence (first {n} numbers): {fibonacci(n)}")
