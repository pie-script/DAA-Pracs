# Practical 1

## Summary
In this practical, we implemented, analyzed, and compared the performance of five key sorting algorithms: **Bubble Sort**, **Selection Sort**, **Insertion Sort**, **Quick Sort**, and **Merge Sort**. 
Using Python's `time.perf_counter()`, we measured the execution times of these algorithms on the same input dataset to observe how they perform in practice and to verify their theoretical time complexities.

## Conclusion
* **$O(N^2)$ Algorithms (Bubble, Selection, Insertion Sort)**: These algorithms are simple to implement and suitable for small datasets. Insertion Sort and Bubble Sort can adapt to already-sorted inputs to run in $O(N)$ time, but their performance degrades rapidly as the dataset size increases.
* **$O(N \log N)$ Algorithms (Quick, Merge Sort)**: These are much faster and more suitable for larger datasets. Merge Sort guarantees stable $O(N \log N)$ sorting but requires $O(N)$ extra helper memory. Quick Sort is extremely fast and works in-place, but has a theoretical worst-case complexity of $O(N^2)$.
* **Overall Selection**: The choice of a sorting algorithm depends on the size of the dataset, whether the data is already partially sorted, memory limits, and the necessity of keeping equal elements in their original order (stability).
