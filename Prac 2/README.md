# Practical 2

## Summary
In this practical, we implemented, analyzed, and compared the performance of two fundamental searching algorithms: **Linear Search** and **Binary Search**. 
Using Python's `time.perf_counter()`, we measured the execution times of these algorithms across different search targets and array sizes to observe their empirical performance and verify their theoretical time complexities.

## Conclusion
* **Linear Search ($O(N)$)**: Linear Search sequentially checks each element in the array until the target is found or the end is reached. It operates on both sorted and unsorted data with $O(1)$ space complexity. However, its execution time scales linearly with the input size $N$, making it inefficient for large datasets.
* **Binary Search ($O(\log N)$)**: Binary Search significantly optimizes search operations by repeatedly dividing the search interval in half. It achieves logarithmic time complexity $O(\log N)$ and $O(1)$ auxiliary space. Its primary constraint is that the input dataset must be pre-sorted.
* **Overall Selection**: Linear Search is best suited for small datasets, unsorted arrays, or single-use searches where sorting overhead is unmotivated. Binary Search is the superior choice for large datasets or scenarios involving frequent lookup operations on sorted data.
