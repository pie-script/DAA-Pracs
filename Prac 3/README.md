# Practical 3

## Summary
In this practical, we implemented, analyzed, and evaluated the **Heap Sort** algorithm using a Max-Heap data structure.
Using Python's `time.perf_counter()`, we measured the execution time of Heap Sort and validated the correctness of the output against Python's built-in `sorted()` function to verify its theoretical time and space complexity characteristics in practice.

## Conclusion
* **Guaranteed Time Complexity**: Heap Sort guarantees a time complexity of $O(N \log N)$ across all scenarios—best case, average case, and worst case. Unlike Quick Sort, its performance never degrades to $O(N^2)$.
* **Space Efficiency**: Heap Sort performs sorting in-place, requiring only $O(1)$ auxiliary space complexity. This makes it more space-efficient than Merge Sort, which requires $O(N)$ auxiliary memory.
* **Trade-offs**: Despite its optimal asymptotic complexity and low space overhead, Heap Sort is generally slower in practice compared to Quick Sort due to poor CPU cache locality caused by non-sequential memory accesses during heapification. Additionally, Heap Sort is an unstable sort.
* **Overall Selection**: Heap Sort is ideal for systems with strict memory constraints and critical real-time performance requirements where worst-case time guarantees ($O(N \log N)$) are essential.
