# Q1 CHEAT LOL

# s = "AABAAB"
# charNum = 0
# sFinal = ""
# for char in s:
#   if charNum == 0 or charNum == 3:
#     True    
#   elif charNum != 0 or charNum != 3:
#     sFinal += char
#   charNum += 1
# print(sFinal)


# Q1 DONE CORRECTLY

# s = "AABAAB"
# prev = ""
# current = ""
# sFinal = ""
# for char in s:
#   prev = char
#   if prev != current:
#     sFinal += char
#   current = char
# print(sFinal)


# Q2

# s1 = "abcde"
# s2 = "abbcd"
# smol = ""
# maxLen = 0
# if len(s1) > len(s2):
#   maxLen = len(s2)
# else:
#   maxLen = len(s1)
# for i in range(0, maxLen):
#   if s1[i] > s2[i]:
#     smol = s2[i]
#   elif s2[i] > s1[i]:
#     smol = s1[i]
#   else:
#     smol = "N/A"
#   print(f"The smaller one is {smol}.")


# Q3

# s1 = "aaaaa"
# s2 = "bbbbbb"
# s3 = ""
# s4 = ""
# placeHolderChar = "0"

# while len(s1) != len(s2):
#   if len(s1) > len(s2):
#     s2 += placeHolderChar
#   else:
#     s1 += placeHolderChar

# for i in range(0,len(s1)):
#   s3 += s1[i]
#   s3 += s2[i]

# for char in s3:
#   if char != placeHolderChar:
#     s4 += char

# print(s4)


# Q4

# maxTry = 10000
# epsilon  = 0.0001

# a = 1
# fa = a ** 3 - a - 3

# b = 2
# fb = b ** 3 - b - 3

# i = 0
# while i < maxTry:
#   c = (a+b) / 2
#   fc = c ** 3 - c - 3

#   if c - a < epsilon or abs(fc) < epsilon:
#     print(f"Solution found at {c} within {i} tries")
#     break

#   i += 1
#   if fc < 0:
#     a = c
#   else:
#     b = c
