
mod=int(1e9)+7
def checkbit(t,i):
    return (t>>i)&1
# i made this intially but later corrected myself checking out the necessary possibilites.
# def solve(a,ind,p):
#     t=0
#     nt=0
#     if(ind>=n):
#         return 0
#     if(p<=a[ind]):
#         t=(solve(a,ind+1,a[ind])+solve(a,ind+1,-float("inf")))
#         return t+1
#     else:
#         nt=solve(a,ind+1,-float("inf"))
#         return nt
#     # return t+nt

# simple recusuion
# def solve(a, ind, p):
#     if ind >= len(a):  # Base condition to end recursion
#         return 0
#     # Option to not take the current element
#     nt = solve(a, ind + 1, p)
#     # Option to take the current element if it forms an increasing sequence
#     t = 0
#     if p <= a[ind]:
#         t = 1 + solve(a, ind + 1, a[ind])
#     # Return the sum of taking and not taking the element
#     return t + nt
# recursion +memo(on values)
# def solve(a, ind, p,dp):
#     if ind >= len(a):  # Base condition to end recursion
#         return 0
#     # Option to not take the current element
#     if((ind,p) in dp):
#         return dp[(ind,p)]
#     nt = solve(a, ind + 1, p,dp)
#     # Option to take the current element if it forms an increasing sequence
#     t = 0
#     if p <= a[ind]:
#         t = 1 + solve(a, ind + 1, a[ind],dp)
#     # Return the sum of taking and not taking the element
#     dp[(ind,p)]=t + nt
#     return t + nt
# recur+memo on indices(Sometimes gives TLE)
# def solve(a, ind, p_index, memo):
#     if ind >= len(a):  # Base case: reached the end of the array
#         return 0
#     # Check if result is already memoized
#     if (ind, p_index) in memo:
#         return memo[(ind, p_index)]
#     # Option to not take the current element
#     nt = solve(a, ind + 1, p_index, memo)
#     # Option to take the current element if it's part of an increasing subsequence
#     t = 0
#     if p_index == -1 or a[p_index] <= a[ind]:
#         t = 1 + solve(a, ind + 1, ind, memo)
#     # Store the result in memo and return
#     memo[(ind, p_index)] = t + nt
#     return memo[(ind, p_index)]


def Non_Decrasing_subsequence(arr,n):
    # count=0
    # subset=[]
    # for i in range(1<<n):
    #     ans=[]
    #     c=0
    #     for j in range(len(arr)):
    #         if(checkbit(i,j)):
    #             ans.append(arr[j])
    #     subset.append(ans)
        # approach-01
        # a=ans[:]
        # ans.sort()
        # if len(ans)!=0 and a==ans:
        #     count+=1
    # approach-02

    # for i in range(len(subset)):
    #     k=0
    #     for j in range(1,len(subset[i])):
    #         if(subset[i][j]<subset[i][j-1]):
    #             k=1
    #             break
    #     if(k==0):
    #         count+=1
    
    # return count-1

    # approach-03
    # using recusion 
    # will tell you by the end of session
    # but will give you partially accepted O(2^n) time complexity
    # return solve(arr,0,-float("inf"))

    # approach-04
    # dp={}
    # return solve(arr,0,-1,dp)

    # approach-05
    # using dynamic programming(Most Optimal)
    dp=[1]*n
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]<=arr[j]):
                dp[j]=(dp[i]+dp[j])%mod
    ans=0
    # print(dp)
    for i in range(n):
        ans=(ans+dp[i])%mod
    return ans
    print(ans)


test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    arr=list(map(int,input().split()))
    print(Non_Decrasing_subsequence(arr,n))