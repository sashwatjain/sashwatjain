"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

def findSubArrays(arr,  n):

    # Array to store all the start and end
    # indices of subarrays with 0 sum
    out = []
    i = 0
    while (i < n):
        prefix = 0
        j = i
        while (j < n):
            prefix += arr[j]
            if (prefix == 0):
                out.append(Pair(i, j))
            j += 1
        i += 1
    return out


def findPages(self, arr, k):
    if len(arr)<k:
        return -1
    l,h,ans=0,sum(arr),-1
    while l<=h:
        mid=(l+h)//2
        if self.isPossible(arr,mid,k):
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans
def isPossible(self,arr,val,k):
    count,curr=1,0
    for pages in arr:
        curr+=pages
        if curr>val:
            curr=pages
            count+=1
        if count>k or pages>val:
            return False
    return True

# Approach:
# Time Complexity:
# Space Complexity:
