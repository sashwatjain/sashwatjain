"""
Day 1 – Permutation Pair Sum
Platform: GFG
Difficulty: Easy 
Date: 2025-11-14

Q: Given two arrays a[] and b[] of equal size and an integer k, Determine whether there exists any permutation of the arrays such that for every index i, the condition a[i] + b[i] ≥ k holds. Return true if such a permutation exists, otherwise return false.
"""

def isPossible(a, b, k):
    
    # Sort a[] in ascending order
    a.sort()
    
    # Sort b[] in descending order
    b.sort(reverse=True)

    # Check if every pair sum >= k
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return False

    return True

if __name__ == '__main__':
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    
    if isPossible(a, b, k):
        print("true")
    else:
        print("false")



"""
Approach:
- here idea is to maximize each pair’s sum efficiently by pairing the smallest element of one array with the largest element of the other.

Sort array a[] in ascending order.
Sort array b[] in descending order.
Now, for every index i, check whether a[i] + b[i] ≥ k. If this condition is true for all pairs, then it’s possible to form a valid permutation return true. If any pair fails to satisfy the condition, return false immediately.

Time Complexity:  O(n log n) due to sorting both arrays.
Space Complexity: O(1) if sorting is done in place;
"""
