# fibonacci.py
def generate_fibonacci(n):
    """Generates the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
        
    return sequence

print("Fibonacci module loaded.")
# Example of how to use it:
# print(generate_fibonacci(10))