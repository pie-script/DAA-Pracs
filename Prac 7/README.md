# Practical 7

## Summary
In this practical, we implemented and analyzed the **Making a Change Problem** using **Dynamic Programming** (Bottom-Up Tabulation approach). 
Given a set of coin denominations and a target change amount $V$, the objective is to determine the minimum number of coins needed to form the change and reconstruct the optimal coin combination.
Using Python's `time.perf_counter()`, we measured the execution time across various target values and coin sets to evaluate performance and verify theoretical complexities.

## Conclusion
* **Dynamic Programming vs Greedy Approach**: While a Greedy approach works for standard canonical coin systems, it fails for general arbitrary coin sets (e.g., coins $\{1, 3, 4\}$ for target amount $6$, where Greedy yields 3 coins $\{4, 1, 1\}$ instead of the optimal 2 coins $\{3, 3\}$). Dynamic Programming guarantees the globally optimal solution for any coin system.
* **Time Complexity ($O(N \cdot V)$)**: The algorithm fills a 1D DP table of size $V+1$ by evaluating each of the $N$ coin options, giving a pseudo-polynomial time complexity of $O(N \cdot V)$.
* **Space Complexity ($O(V)$)**: Storing the minimum coin counts and optimal state transitions up to target amount $V$ requires $O(V)$ auxiliary space.
* **Overall Selection**: The Dynamic Programming approach is the definitive method for solving the general Coin Change problem reliably and optimally.
