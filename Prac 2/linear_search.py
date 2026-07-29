import time

def linear_search(arr, target):
    """
    Linear Search Algorithm:
    Iterates through the list element by element to find the target.
    
    Time Complexity:
      - Best Case:    O(1) (when target is the first element)
      - Average Case: O(N) (when target is in the middle)
      - Worst Case:   O(N) (when target is the last element or not present)
      
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the element
    return -1  # Return -1 if target is not found

def main():
    print("========================================")
    print("             LINEAR SEARCH              ")
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

    try:
        target = int(input("Enter target element to search for: "))
    except ValueError:
        print("Error: Target must be an integer.")
        return

    print(f"\nOriginal Array: {arr}")
    print(f"Array Size (N): {len(arr)}")
    print(f"Target Element: {target}\n")

    # Time measurement
    start_time = time.perf_counter()
    index = linear_search(arr, target)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    if index != -1:
        print(f"Result:         Target found at index {index}")
    else:
        print("Result:         Target not found in the array")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(1)")
    print("  - Average Case: O(N)")
    print("  - Worst Case:   O(N)")
    print("Theoretical Space Complexity: O(1)")
    print("========================================")

if __name__ == "__main__":
    main()
