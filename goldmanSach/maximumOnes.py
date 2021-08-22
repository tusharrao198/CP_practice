"""
Karan got bored, so he invented a game to be played on paper. He writes n integers a1, a2, …, an. Each of those integers can be either 0 or 1. He’s allowed to do exactly one move: he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j] (that is i ≤ k ≤ j). Flip the value of x means to apply operation x = 1 – x.
The goal of the game is that after exactly one move to obtain the maximum number of ones. Write a program to solve the little game of Iahub.

Input

The first line of the input contains an integer n (1 ≤ n ≤ 100). In the second line of the input there are n integers: a1, a2, …, an. It is guaranteed that each of those n values is either 0 or 1.
Output

Print an integer — the maximal number of 1s that can be obtained after exactly one move.
 
Examples

Input
5
1 0 0 1 0
Output
4
 

Input
4
1 0 0 1
Output
4
Note

In the first case, flip the segment from 2 to 5 (i = 2, j = 5). That flip changes the sequence, it becomes: [1 1 1 0 1]. So, it contains four ones. There is no way to make the whole sequence equal to [1 1 1 1 1].
In the second case, flipping only the second and the third element (i = 2, j = 3) will turn all numbers into 1.
 
"""


def solve(n, arr):
    original_ones = 0
    max_, cur = 0, 0 
    for i in range(n):
        if arr[i]==0:
            arr[i] = 1
        else: 
            arr[i] = -1
            original_ones+=1

        cur = max(cur+arr[i], arr[i])
        max_ = max(max_, cur)
        
        # print(max_)

    max_ = max(0, max_)
    print("A = ",original_ones)
    return original_ones + max_


n = 5
arr = [1,0,0,0,1]
# arr = [1,0,0,1,0]

print(solve(n, arr))
