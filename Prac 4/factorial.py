import time
import sys

# Increase recursion depth limit for handling larger n if needed
sys.setrecursionlimit(2000)

def factorial_iterative(n):
    """
    Iterative Factorial Algorithm:
    Computes n! by multiplying numbers from 1 to n in a loop.
    
    Time Complexity:  O(N) - N multiplications
    Space Complexity: O(1) - Constant auxiliary space
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Recursive Factorial Algorithm:
    Computes n! using recurrence relation: n! = n * (n - 1)! with base case 0! = 1.
    
    Time Complexity:  O(N) - N recursive calls
    Space Complexity: O(N) - Auxiliary space due to call stack frames
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("========================================")
    print("         FACTORIAL PROGRAM (DAA)        ")
    print("========================================")
    
    user_input = input("Enter a non-negative integer (N): ").strip()
    if not user_input:
        print("Error: Input is empty.")
        return
        
    try:
        n = int(user_input)
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative integer.")
        return

    print(f"\nCalculating Factorial for N = {n}...\n")

    # Time measurement for Iterative Approach
    start_time_iter = time.perf_counter()
    result_iter = factorial_iterative(n)
    end_time_iter = time.perf_counter()
    time_iter_us = (end_time_iter - start_time_iter) * 1_000_000

    # Time measurement for Recursive Approach
    try:
        start_time_rec = time.perf_counter()
        result_rec = factorial_recursive(n)
        end_time_rec = time.perf_counter()
        time_rec_us = (end_time_rec - start_time_rec) * 1_000_000
    except RecursionError:
        print("Error: Maximum recursion depth exceeded in recursive method.")
        result_rec = None
        time_rec_us = float('inf')

    # Verification
    if result_rec is not None:
        assert result_iter == result_rec, "Error: Iterative and Recursive results do not match!"

    print("----------------------------------------")
    print("RESULTS:")
    print("----------------------------------------")
    # Truncate string output if number is huge for display cleanliness
    str_res = str(result_iter)
    if len(str_res) > 50:
        print(f"Result (N!):     {str_res[:20]}...{str_res[-20:]} ({len(str_res)} digits)")
    else:
        print(f"Result (N!):     {result_iter}")
        
    print("----------------------------------------")
    print("EXECUTION TIME COMPARISON:")
    print(f"  - Iterative Method: {time_iter_us:.2f} µs")
    if result_rec is not None:
        print(f"  - Recursive Method: {time_rec_us:.2f} µs")
    else:
        print("  - Recursive Method: Exceeded recursion depth limit")
    print("----------------------------------------")
    print("THEORETICAL COMPLEXITY ANALYSIS:")
    print("Iterative Approach:")
    print("  - Time Complexity:  O(N)")
    print("  - Space Complexity: O(1)")
    print("Recursive Approach:")
    print("  - Time Complexity:  O(N)")
    print("  - Space Complexity: O(N) [Stack Frames]")
    print("========================================")

if __name__ == "__main__":
    main()
