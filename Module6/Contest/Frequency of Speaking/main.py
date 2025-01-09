#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to count frequency of words
def frequency_word(statement):
    words = statement.copy()
    countedwithvalue={}
    for word in words:
        count=words.count(word)
        countedwithvalue[word]=count
    for key,value in countedwithvalue.items():
        if value==1:
            print(key)
        else:
            print(key,value)
    # Your code here

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    # testcase input
    testcase = int(input())
    
    # loop to iterate through testcases
    while testcase > 0:
        statement = input().split()
        frequency_word(statement)
        
        testcase -= 1


        print("~")
if __name__ == '__main__':
    main()
# } Driver Code Ends