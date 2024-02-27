# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.


# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def roman(s):

    hashMap = {
        "I" :1,
"V":5,
"X"  :10,
"L"  :50,
"C"  :100,
"D"  :500,
"M"  :1000,
    }

    total = 0 
    i = len(s)-1

    while i >= 0:
        if (hashMap[s[i]] <= hashMap[s[i-1]]) or (i == 0) :
            total+=hashMap[s[i]]
            print(s[i])
            i-=1
        else:
            total += (hashMap[s[i]] - hashMap[s[i-1]])
            i -= 2


            
        
    print(total)
    
             

roman("LVIII")
roman("MMMDCCCLXXXVIII")