"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""
# Python Implementation to Find the maximum 
# number possible after at most `k` swaps 
# using Recursion with focused digit placement.

# Function to keep the maximum result
def match(curr, res):
  
    # If current number is larger, update result
    if curr > res:
        res = curr
    return res

# Function to set highest possible digits
# at given index
def setDigit(s, index, res, k):
  
    # Base case: If no swaps left or index reaches 
    # the last character, update result
    if k == 0 or index == len(s) - 1:
        res = match(s, res)
        return res

    maxDigit = 0

    # Finding maximum digit for placing at given index
    for i in range(index, len(s)):
        maxDigit = max(maxDigit, int(s[i]))

    # If the digit at current index is already max
    if int(s[index]) == maxDigit:
        res = setDigit(s, index + 1, res, k)
        return res

    # Try swapping with the maximum digit found
    for i in range(index + 1, len(s)):
      
        # If max digit is found at current position
        if int(s[i]) == maxDigit:
          
            # Swap to get the max digit at the required index
            s = swap(s, index, i)

            # Call the recursive function to set the next digit
            res = setDigit(s, index + 1, res, k - 1)

            # Backtrack: swap the digits back
            s = swap(s, index, i)

    return res

# Function to swap characters in the string
def swap(s, i, j):
  
    # Convert string to list for mutation,
    # then back to string
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

# Function to find the largest number after k swaps
def findMaximumNum(s, k):
    res = s
    res = setDigit(s, 0, res, k)

    # Returning the result
    return res

if __name__ == "__main__":
  
    s = "7599"  
    k = 2
    print(findMaximumNum(s, k))
    
    
# Python program to implement 
# Cryptarithmetic Puzzle Solver

# Function to remove preceding zeroes
def removeZeroes(a):
    return a.lstrip('0') or '0'

# function change character string
# to digit string
def charToDigit(a, digits):
    return ''.join(digits[ord(c) - ord('a')] for c in a)

# function to find sum of numbers
# in the form of strings
def findSum(a, b):
    if len(a) > len(b):
        a, b = b, a

    str_res = []
    carry = 0

    for i in range(len(a)):
        sum_digit = int(a[-1 - i]) + int(b[-1 - i]) + carry
        str_res.append(str(sum_digit % 10))
        carry = sum_digit // 10

    for i in range(len(a), len(b)):
        sum_digit = int(b[-1 - i]) + carry
        str_res.append(str(sum_digit % 10))
        carry = sum_digit // 10

    if carry:
        str_res.append(str(carry))

    return removeZeroes(''.join(reversed(str_res)))

# function to check if puzzle is solved
def isSolved(a, b, sum, digits):
    x = charToDigit(a, digits)
    y = charToDigit(b, digits)
    z = charToDigit(sum, digits)

    res = findSum(x, y)
    z = removeZeroes(z)

    return z == res

# Function to solve Cryptarithmetic
# Puzzle using backtracking
def cryptarithmeticSolver(ind, digits, characters, a, b, sum):
    if ind == 26:
        return isSolved(a, b, sum, digits)

    if digits[ind] != '+':
        return cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum)

    # Try assigning digits only for characters that haven't been assigned yet
    for i in range(10):
        if characters[i] == 0:
            characters[i] = 1
            digits[ind] = str(i)
            if cryptarithmeticSolver(ind + 1, digits, characters, a, b, sum):
                return True
            digits[ind] = '+'
            characters[i] = 0

    return False

# Function to solve Cryptarithmetic Puzzle
def solvePuzzle(a, b, sum):
    digits = ['-' for _ in range(26)]
    characters = [0] * 10

    for c in a + b + sum:
        digits[ord(c) - ord('a')] = '+'

    if cryptarithmeticSolver(0, digits, characters, a, b, sum):
        x = charToDigit(a, digits)
        y = charToDigit(b, digits)
        res = charToDigit(sum, digits)
        return [x, y, res]
    else:
        return ["-1"]

# Driver Code
a = "s"
b = "p"
sum = "f"
ans = solvePuzzle(a, b, sum)
print(" ".join(ans))
# Approach:
# Time Complexity:
# Space Complexity:
