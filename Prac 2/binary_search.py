import time

def binary_search(arr, target):
    """
    Binary Search Algorithm (Iterative):
    Repeatedly divides the search space in half to locate the target.
    Prerequisite: The array MUST be sorted.
    
    Time Complexity:
      - Best Case:    O(1) (when target is at the midpoint of the array)
      - Average Case: O(log N)
      - Worst Case:   O(log N)
      
    Space Complexity: O(1) (Iterative approach uses constant auxiliary space)
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # Use low + (high - low) // 2 to prevent potential overflow in general context
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid  # Return the index of the element
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Return -1 if target is not found

def main():
    print("========================================")
    print("             BINARY SEARCH              ")
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

    # Binary search requires sorted array, so we sort it first
    # We will inform the user and show the sorted array
    sorted_arr = sorted(arr)
    print(f"\nOriginal Array: {arr}")
    print(f"Sorted Array:   {sorted_arr} (Required for Binary Search)")
    print(f"Array Size (N): {len(sorted_arr)}")
    print(f"Target Element: {target}\n")

    # Time measurement (excluding sorting time)
    start_time = time.perf_counter()
    index = binary_search(sorted_arr, target)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    if index != -1:
        print(f"Result:         Target found at index {index} in sorted array")
    else:
        print("Result:         Target not found in the array")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(1)")
    print("  - Average Case: O(log N)")
    print("  - Worst Case:   O(log N)")
    print("Theoretical Space Complexity: O(1)")
    print("========================================")

if __name__ == "__main__":
    main()
