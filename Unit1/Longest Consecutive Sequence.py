# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# # Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

#


def lcs(nums):
    longestStreak = 0 
    hashSet = set(nums)

    for i in hashSet:
        if i - 1 not in hashSet:
            curr = i 
            currStreak = 1
            while curr + 1 in hashSet:
                curr += 1
                currStreak +=1
            longestStreak = max(longestStreak,currStreak)
    return longestStreak

            


print(lcs(nums = [100,4,200,1,3,2]))
print(lcs(nums = [0,3,7,2,5,8,4,6,0,1]))

print(lcs(nums = []))
