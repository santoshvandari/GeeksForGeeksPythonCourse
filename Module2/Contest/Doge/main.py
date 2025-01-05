#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def doge_count(str):
    count = 0
    alphabet = [chr(letter) for letter in range(ord('a'),ord('z')+1)]
    for alp  in alphabet:
        word = f"do{alp}e"
        count = count + str.count(word)
    

    ##Your code here
    return count

#{ 
 # Driver Code Starts.



def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(doge_count(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends