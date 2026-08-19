import time

def min_coins_make_change(coins, amount):
    """
    Dynamic Programming - Making a Change Problem (Bottom-Up Tabulation)
    
    Finds the minimum number of coins needed to make a given target amount,
    and reconstructs the optimal set of coins used.
    
    Time Complexity:  O(N * V) where N is number of coins, V is target amount
    Space Complexity: O(V) for the DP table and parent tracking array
    """
    if amount < 0:
        return -1, [], []
    if amount == 0:
        return 0, [], [0]

    # dp[i] will store the minimum coins needed for amount i
    # Initialize DP array with infinity
    INF = float('inf')
    dp = [INF] * (amount + 1)
    
    # parent[i] will store the coin denomination used to reach amount i optimal state
    parent = [-1] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Build the DP table bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    # If dp[amount] is still INF, amount cannot be formed
    if dp[amount] == INF:
        return -1, [], dp

    # Reconstruct the optimal coin combination
    used_coins = []
    curr = amount
    while curr > 0:
        coin_used = parent[curr]
        used_coins.append(coin_used)
        curr -= coin_used

    return dp[amount], used_coins, dp

def main():
    print("========================================")
    print("  MAKING A CHANGE PROBLEM (DYNAMIC PROG)")
    print("========================================")
    
    # Get Coin Denominations
    coins_input = input("Enter coin denominations (separated by spaces or commas): ").strip()
    if not coins_input:
        print("Error: Input is empty.")
        return
        
    try:
        cleaned_coins = coins_input.replace(',', ' ')
        coins = [int(x) for x in cleaned_coins.split()]
        if not coins:
            print("Error: No valid coins provided.")
            return
        # Filter out non-positive coins
        coins = [c for c in coins if c > 0]
        if not coins:
            print("Error: Coin denominations must be positive integers.")
            return
    except ValueError:
        print("Error: Invalid coin input. Please enter integers only.")
        return

    # Get Target Amount
    try:
        amount = int(input("Enter target change amount (V): "))
        if amount < 0:
            print("Error: Target amount cannot be negative.")
            return
    except ValueError:
        print("Error: Target amount must be an integer.")
        return

    print(f"\nCoin Denominations: {sorted(coins)}")
    print(f"Target Amount (V):  {amount}\n")

    # Measure execution time
    start_time = time.perf_counter()
    min_coins, used_coins, dp_table = min_coins_make_change(coins, amount)
    end_time = time.perf_counter()
    
    elapsed_time_us = (end_time - start_time) * 1_000_000

    print("----------------------------------------")
    if min_coins != -1:
        print(f"Status:                 SUCCESS")
        print(f"Minimum Coins Required: {min_coins}")
        print(f"Coins Used:             {used_coins}")
        
        # Display DP Table slice for reference if amount is reasonable
        if amount <= 30:
            print(f"DP Table dp[0..{amount}]:   {dp_table}")
        else:
            print(f"DP Table Sample dp[0..10]: {dp_table[:11]} ... dp[{amount}] = {dp_table[amount]}")
    else:
        print("Status:                 IMPOSSIBLE")
        print(f"Target amount {amount} cannot be formed using the given coin denominations.")
        
    print(f"Execution Time:         {elapsed_time_us:.2f} µs")
    print("----------------------------------------")
    print("THEORETICAL COMPLEXITY ANALYSIS:")
    print(f"  - Time Complexity:  O(N * V)  [N = {len(coins)} coins, V = {amount} amount]")
    print(f"  - Space Complexity: O(V)      [DP table size {amount + 1}]")
    print("========================================")

if __name__ == "__main__":
    main()
