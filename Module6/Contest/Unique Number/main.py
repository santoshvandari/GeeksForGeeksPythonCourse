#User function Template for python3

# Function to print elements in sorted order
def sorted_elements(arr):
    
    # Your code here
    # return the list which contains 
    # elements in sorted order
    newarr=(list(set(arr)))
    newarr.sort()
    return newarr


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Driver Code
def main():
    testcase = int(input())

    while testcase > 0:
        N = int(input())
        arr = list(map(int, input().split()))
        l = sorted_elements(arr)

        for x in l:
            print(x, end=' ')

        print()
        testcase -= 1

        print("~")


if __name__ == '__main__':
    main()

# } Driver Code Ends