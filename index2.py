## Vowel vs Consonant
## Function to count vowels and consonants

# t = int(input())
# for _ in range(t):
# 	s = input()
# 	vowels = 0
# 	consonants = 0
# 	for ch in s:
# 		if ch.lower() in 'aeiou':
# 			vowels += 1
# 		elif ch.isalpha():
# 			consonants += 1
# 	print(f"{vowels}{consonants}")

#sub array=continous part of an array is called a subarray
# a single element is also a sub array
#entire array is also called a sub array ,empty array cannot be a sub array

#arr=[4,2,10,3,12-2,15]
#count of sub array
#sub arrray srarting from iindex zero=[4,2,10,3,12,-2,15]

# given an array element how many sub array can be generated n(n+1)/2 where n is the length of array'
#print all the values of the sub array
#find the sum of all the elements in the  given sub array
#given an array A of N non negative numbers and a non negative number B you need to find number of sub arrays in A with a sum less then B
# A=[2,,5,6]
# B=10
# count=0
# for i in range(len(A)):
#   sum=0
# for j in range(i,len(A)):
#     sum+=A[i]
#     if(sum<B):
#         count+=1
# print(i)        
#given an array of integer of A a sub array of an array is said to be good if it fullfills any one of the criteria
#condition 1= length of the sub array is to be even and the sum of all the elements of the sub array must be less then B
#2=length of the sub array is to be odd and the sum of all the elements of the sub array must be greater then B 
#you need to find the count of good sub array in A
# def countGoodSubarrays(A, B):
#     n = len(A)
#     count = 0    
#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total += A[j]       
#             length = j - i + 1   
#             if (length % 2 == 0 and total < B) or (length % 2 == 1 and total > B):
#                 count += 1
#     return count

# A = [2,5,6,7,8]
# B = 10
# result = countGoodSubarrays(A, B)
#print("count of Good Subarrays =",result)
# A = [1,2,3,4,5]
# B = 4
# N = len(A)
# count = 0
# for i in range(N):
#     sum1 = 0
#     for j in range(i,N):
#         sum1 += A[j]
#         if sum1 < B and (j - i + 1) % 2 == 0:
#             count += 1
#         if sum1 > B and (j - i + 1) % 2 != 0:
#             count += 1
#     print("count of Good Subarrays :",count)        

# A=5
# C=[2,1,3,4,5]
# B=12

#2.LengthofString-II
# Youhaveastring(A).Youhavetoprintlengthofinputstring
# A=int(input("enter a string="))
# print(len(A))

#  3.IsisPalindrome?
#  WriteaprogramtoinputTstrings(S)fromuserandprint1ifitispalindromeotherwiseprint0.
#  NOTE:Astringispalindromeifitreadsthesamefrombackwardasfromforward.
#  Input:
#  3
#  abcba
#  axax
#  abb
# T=int(input("enter a string:"))
# for i in range(T):
#     s=input("enter a string=")
#     if s==s[::-1]:
#         print(1)
#     else:
#         print(0)    



# 4.Trim (*)
#  You are given a character string A. You to trim both leading and trailing asterisk characters('*') in
#  the string and print the resultant string.
#  Input:
#  A="**h*e*l*lo*"
#  Output
# A="**h*e*l*lo*"
# print(A.strip('*'))

#  5.Trim left (*)
#  You are given a character string A. You to trim leading asterisk characters('*') in the string and
#  print the resultant string.
#  Input:
#  A="**h*e*l*lo*"
#  Output:
#  h*e*l*lo*
# A="**h*e*l*lo*"
# print(A.lstrip('*'))

#  6.Trim right (*)
#  You are given a character string A. You to trim trailing asterisk characters('*') in the string and
#  print the resultant string.
#  Input:
#  A="**h*e*l*lo*"
#  Output:
#  **h*e*l*l
# A="**h*e*l*lo*"
# print(A.rstrip('*'))

# 7.Reverse the word
#  You are given string (A) and you have to print after reversing that.
#  Input:
#  String
#   Output
# A=input()
# print(A[::-1])

#  8.Reverse the order of words
#  You are given string (A) and you have to print the reverse order of words.
#  Input:
#  Suyash Chaudhary
#  Output:
#  Chaudhary Suyash
# Input
# A = input("Enter a string: ")
# print(' '.join(A.split()[::-1]))

#  9.Reverse string
#  Write a program to reverse the words present in a string. Check example input/output.
#  Input:
#  Everyone loves data science
#  Output:
#  enoyrevE sevol atad ecneic
#A = input("Enter a string: ")
#print(A[::-1])

#10
#A = "PythoN"
# Convert to lowercase
#print(A.lower())

# Q11.toupper()
# The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.
# Print the uppercase version of the given the string.
# A="pYthON"
# print(A.upper())

# # Q12.Isalnum()
# # Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, print 0. 
# A=input("Enter a string: ")
# if A.isalnum():
#     print(1)
# else:
#     print(0)

# # Q13 Isalpha()
# # Print 1 if all the characters of the character array are alphabetical (a-z and A-Z), else print 0.
# A=input("Enter a String: ")
# if A.isalpha():
#     print(1)
# else:
#     print(0)

# # Q14.First Occurrence
# #  You are given a character string A, having length N and an integer ASCII code B.
# #  You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or
# #  report that it does not exist.

# A="aabbcc"
# B=98
# ch=chr(B)
# if ch in A:
#     print(A.index(ch))
# else:
#     print("does not exist")

# #Q15.First Occurrence Of Word
# #  You are given two character strings A and B.
# #  You have to find the first occurrence of string B in string A, as a substring, and return the starting
# #  position of first occurrence.
# #  Asubstring is a contiguous sequence of characters within a string. For e.g "at" is a substring in
# #  "catalogue".

# A="aabababaa"
# B="ba"
# if B in A:
#     print(A.index(B))
# else:
#     print("does not exist")

# # Q16..Count Occurrences
# #  Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
# A= input("Enter a String: ")
# count=0
# for i in range(len(A) -2 ):
#     if A[i:i+3]=="bob":
#         count +=1
# print(count)


#  17.String operations
#  Akash likes playing with strings. One day he thought of applying following operations on the
#  string in the given order:
#  Concatenate the string with itself.
#  Delete all the uppercase letters.
#  Replace each vowel with '#'.
#  You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
#  resultant string after applying the above operations.
#  NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
#  Input:
#  A="aeiOUz"
#  Output:
#  "###z###z

# A = "aeiOUz"
# A = A + A
# A = ''.join(ch for ch in A if not ch.isupper())
# vowels = 'aeiou'
# A = ''.join('#' if ch in vowels else ch for ch in A)
# print(A)
