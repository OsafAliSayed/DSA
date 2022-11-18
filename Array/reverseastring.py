# https://practice.geeksforgeeks.org/problems/reverse-an-array/0
# code
T = int(input())
for i in range(T):
    l = int(input())
    arr = [int(i) for i in input().split()]
    
    for i in arr[::-1]:
        print(i, end=" ")
    print()