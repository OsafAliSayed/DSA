# https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
#User function Template for python3

from functools import reduce
def getMinMax( a, n):
    max = reduce(lambda x, y:  y if y > x else x, a)
    min = reduce(lambda x, y: x if y > x else y, a)
    return [max, min]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product, end=" ")

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends