#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to join given strings
def combo_string(a, b):
    
    
  longer=a
  short=b
  
  if(len(a)<len(b)):
      longer=b
      short=a
  
  # your code here
  
  return short+longer+short

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    # 
    testcases = int(input())
    
    while(testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        
        testcases -= 1
        
        print (combo_string(string1, string2))

        print("~")
if __name__ == '__main__':
    main()
# } Driver Code Ends