import time

def selection_sort(arr):
    """
    Selection Sort algorithm.
    Repeatedly finds the minimum element and places it at the beginning.
    """
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def main():
    print("========================================")
    print("            SELECTION SORT              ")
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
    sorted_arr = selection_sort(arr)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(N^2)")
    print("  - Average Case: O(N^2)")
    print("  - Worst Case:   O(N^2)")
    print("Theoretical Space Complexity: O(1)")
    print("========================================")

if __name__ == "__main__":
    main()
