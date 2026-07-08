import time
import sys

# Increase recursion depth for Quick Sort and Merge Sort on large inputs
sys.setrecursionlimit(200000)

def bubble_sort(arr):
    """
    Bubble Sort:
    Best Case Complexity: O(N) (when array is already sorted)
    Average Case Complexity: O(N^2)
    Worst Case Complexity: O(N^2)
    """
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(arr):
    """
    Selection Sort:
    Best Case Complexity: O(N^2)
    Average Case Complexity: O(N^2)
    Worst Case Complexity: O(N^2)
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

def insertion_sort(arr):
    """
    Insertion Sort:
    Best Case Complexity: O(N) (when array is already sorted)
    Average Case Complexity: O(N^2)
    Worst Case Complexity: O(N^2)
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

def quick_sort(arr):
    """
    Quick Sort:
    Best Case Complexity: O(N log N)
    Average Case Complexity: O(N log N)
    Worst Case Complexity: O(N^2)
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

def merge_sort(arr):
    """
    Merge Sort:
    Best Case Complexity: O(N log N)
    Average Case Complexity: O(N log N)
    Worst Case Complexity: O(N log N)
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
    print("     SORTING ALGORITHMS TIME ANALYSIS   ")
    print("========================================")
    
    # Get user input for the array
    user_input = input("Enter array elements (separated by spaces or commas): ").strip()
    if not user_input:
        print("Error: Input is empty.")
        return
        
    try:
        # Replace commas with spaces and split into integers
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

    # Define algorithms to test
    algorithms = [
        ("Bubble Sort", bubble_sort, "Best: O(N) | Avg: O(N^2) | Worst: O(N^2)"),
        ("Selection Sort", selection_sort, "Best: O(N^2) | Avg: O(N^2) | Worst: O(N^2)"),
        ("Insertion Sort", insertion_sort, "Best: O(N) | Avg: O(N^2) | Worst: O(N^2)"),
        ("Quick Sort", quick_sort, "Best: O(N log N) | Avg: O(N log N) | Worst: O(N^2)"),
        ("Merge Sort", merge_sort, "Best: O(N log N) | Avg: O(N log N) | Worst: O(N log N)")
    ]

    # Print execution results header
    print(f"{'Algorithm':<16} | {'Execution Time':<18} | {'Theoretical Complexity (Time)'}")
    print("-" * 75)

    sorted_arr = []
    for name, func, complexity in algorithms:
        # Measure time
        start_time = time.perf_counter()
        res = func(arr)
        end_time = time.perf_counter()
        
        elapsed_seconds = end_time - start_time
        # Convert to microseconds for better readability on small arrays
        elapsed_microseconds = elapsed_seconds * 1_000_000
        
        print(f"{name:<16} | {elapsed_microseconds:.2f} µs          | {complexity}")
        
        # Save sorted result to display
        sorted_arr = res

    # Verify sorting correctness
    assert sorted_arr == sorted(arr), "Error: Sorting algorithm output is incorrect!"
    print("-" * 75)
    print(f"Sorted Array: {sorted_arr}\n")

if __name__ == "__main__":
    main()
