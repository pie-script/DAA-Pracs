import time

def heapify(arr, n, i):
    """
    To heapify a subtree rooted at index i, which is an index in arr[].
    n is the size of the heap.
    Maintains the Max-Heap property: Parent >= Left Child and Parent >= Right Child.
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # left child = 2*i + 1
    right = 2 * i + 2    # right child = 2*i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def max_heap_sort(arr):
    """
    Max Heap Sort Algorithm.
    1. Build a max heap from the input array.
    2. At this point, the largest element is stored at the root (index 0).
    3. Swap root with the last element of the heap and reduce heap size by 1.
    4. Heapify the root of the tree to restore max heap property.
    5. Repeat until the heap size is 1.
    """
    n = len(arr)
    a = arr.copy()

    # Step 1: Build a max heap (rearrange array)
    # Start from the last non-leaf node down to root
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # Step 2: One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum element) to the end
        a[0], a[i] = a[i], a[0]

        # Call max heapify on the reduced heap
        heapify(a, i, 0)

    return a

def main():
    print("========================================")
    print("            MAX HEAP SORT               ")
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
    sorted_arr = max_heap_sort(arr)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    # Verification against built-in sort
    assert sorted_arr == sorted(arr), "Error: Max Heap Sort output is incorrect!"

    print("----------------------------------------")
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Execution Time: {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("Theoretical Time Complexity:")
    print("  - Best Case:    O(N log N)")
    print("  - Average Case: O(N log N)")
    print("  - Worst Case:   O(N log N)")
    print("Theoretical Space Complexity: O(1) auxiliary space (In-place)")
    print("========================================")

if __name__ == "__main__":
    main()
