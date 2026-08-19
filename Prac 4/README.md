# Practical 4

## Summary
In this practical, we implemented, analyzed, and compared the performance of calculating the factorial of a non-negative integer $N$ ($N!$) using both **Iterative** and **Recursive** approaches. 
Using Python's `time.perf_counter()`, we measured the execution times of both methods across various input values of $N$ to observe their practical performance and verify their theoretical time and space complexities.

## Conclusion
* **Iterative Method ($O(N)$ Time, $O(1)$ Space)**: The iterative approach uses a single loop to compute $N!$. It requires constant auxiliary space $O(1)$ and avoids call stack overhead, making it faster and free from stack overflow limitations for large values of $N$.
* **Recursive Method ($O(N)$ Time, $O(N)$ Space)**: The recursive approach relies on the mathematical recurrence relation $N! = N \times (N-1)!$. Each call adds a frame to the call stack, leading to $O(N)$ space complexity and risk of `RecursionError` for large inputs.
* **Overall Selection**: The iterative method is superior for practical implementation due to lower memory consumption, faster execution, and safety against call-stack limits.
