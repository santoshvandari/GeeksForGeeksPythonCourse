#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to print elements in sorted order
def find_lonely(numbers, K):
    # Your code here
    number=None
    for i in numbers:
        valuecount = numbers.count(i)
        if valuecount != K:
              number=i
    if not number:
        print(-1)
    else:
        print(number)

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    testcase = int(input())
    
    while testcase > 0:
        K = int(input())
        numbers = input().split()
        find_lonely(numbers, K)
        
        testcase -= 1


        print("~")
if __name__ == '__main__':
    main()
# } Driver Code Ends