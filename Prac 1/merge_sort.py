import time
import sys

# Increase recursion depth for deep recursion on large inputs
sys.setrecursionlimit(200000)

def merge_sort(arr):
    """
    Merge Sort algorithm (recursive).
    Divides the array into two halves, recursively sorts them,
    and then merges the sorted halves.
    """
    def _merge_sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _merge_sort(a[:mid])
        right = _merge_sort(a[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return _merge_sort(arr.copy())

def main():
    print("========================================")
    print("              MERGE SORT                ")
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
    sorted_arr = merge_sort(arr)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(N log N)")
    print("  - Average Case: O(N log N)")
    print("  - Worst Case:   O(N log N)")
    print("Theoretical Space Complexity: O(N) auxiliary space")
    print("========================================")

if __name__ == "__main__":
    main()
