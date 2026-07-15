import time

def insertion_sort(arr):
    """
    Insertion Sort algorithm.
    Inserts each element into its correct position in a sorted subarray.
    """
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def main():
    print("========================================")
    print("            INSERTION SORT              ")
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
    sorted_arr = insertion_sort(arr)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(N) (when already sorted)")
    print("  - Average Case: O(N^2)")
    print("  - Worst Case:   O(N^2)")
    print("Theoretical Space Complexity: O(1)")
    print("========================================")

if __name__ == "__main__":
    main()
