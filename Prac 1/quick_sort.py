import time
import sys

# Increase recursion depth for deep recursion on large inputs
sys.setrecursionlimit(200000)

def quick_sort(arr):
    """
    Quick Sort algorithm (In-place recursive partitioning).
    Uses a middle pivot to avoid worst-case O(N^2) on sorted inputs.
    """
    a = arr.copy()
    def _quick_sort(lst, low, high):
        if low < high:
            pi = partition(lst, low, high)
            _quick_sort(lst, low, pi - 1)
            _quick_sort(lst, pi + 1, high)
            
    def partition(lst, low, high):
        mid = (low + high) // 2
        lst[mid], lst[high] = lst[high], lst[mid]
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    _quick_sort(a, 0, len(a) - 1)
    return a

def main():
    print("========================================")
    print("              QUICK SORT                ")
    print("========================================")
    
    user_input = input("Enter array elements (separated by spaces or commas): ").strip()
    if not user_input:
        print("Error: Input is empty.")
        return
        
    try:
        cleaned_input = user_input.replace(',', ' ')
        arr = [int(x) for x in cleaned_input.split()]
        if not arr:
            print("Error: No valid numbers found.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
        return

    print(f"\nOriginal Array: {arr}")
    print(f"Array Size (N): {len(arr)}\n")

    # Time measurement
    start_time = time.perf_counter()
    sorted_arr = quick_sort(arr)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(N log N)")
    print("  - Average Case: O(N log N)")
    print("  - Worst Case:   O(N^2)")
    print("Theoretical Space Complexity: O(log N) auxiliary space")
    print("========================================")

if __name__ == "__main__":
    main()
