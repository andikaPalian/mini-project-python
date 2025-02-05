def maxChar(str):
    charMap = {}
    for char in str:
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1
            
    maxCount = 0
    maxChar = ""
    for char, count in charMap.items():
        if (count > maxCount):
            maxCount = count
            maxChar = char
        
    return maxChar

print(maxChar("abccccdddddddeeeeeeeee"))