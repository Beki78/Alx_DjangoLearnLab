# # # # def mergeAlternately( word1: str, word2: str) -> str:
# # # #         i , j = 0, 0
# # # #         while i < len(word1) and j < len(word2):
# # # #             ans = i , j == word1[i], word2[2]
# # # #             print(ans)
# # # # mergeAlternately("ab", "pqrs")

# # # def count_occurrences(arr):
# # #     # Initialize an empty hash table (dictionary)
# # #     hash_table = {}
# # #     maximum = max(arr)

# # #     # Iterate through each element in the array
# # #     for element in arr:
# # #         # If the element is already in the hash table, increment its count
# # #         if element in hash_table:
# # #             hash_table[element] += 1
# # #         # If the element is not in the hash table, add it with a count of 1
# # #         else:
# # #             hash_table[element] = 1
    
# # #     ans = hash_table[maximum]

# # #     return hash_table

# # # # Example usage:
# # # arr = [3,2,3]
# # # occurrences = count_occurrences(arr)
# # # print(occurrences)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

# # def count_occurrences(arr):
# #     # Initialize an empty hash table (dictionary)
# #     hash_table = {}

# #     # Iterate through each element in the array
# #     for element in arr:
# #         # If the element is already in the hash table, increment its count
# #         if element in hash_table:
# #             hash_table[element] += 1
# #         # If the element is not in the hash table, add it with a count of 1
# #         else:
# #             hash_table[element] = 1

# #     # Find the key with the highest value in the hash table
# #     most_occurrences = max(hash_table, key=hash_table.get)

# #     return hash_table, most_occurrences

# # # Example usage:
# # arr = [2,2,1,1,1,2,2]
# # occurrences, most_occurrences = count_occurrences(arr)
# # # print(occurrences)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
# # print(most_occurrences)  # Output: 4


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         #cast it to list 
#         #sort the lists
#         #loop through the s list and check if all elements in list a exists in list b
        
#         lst_a = list(s)
#         lst_b = list(t)
#         lst_a.sort()
#         lst_b.sort()

#         for i in lst_a:
#             if i not in lst_b:
#                 return False
#         return True
# sol = Solution()
# print(sol.isSubsequence("abc", "cab"))


# def hashed (a, b):
#     hash_table = {}
#     for i in a:
#         for j in b:
#             if i == j:
#                 print(i,j)
#                 hash_table[i,j] = i, j
#     return hash_table
# print(hashed("aA", "aAAbbbb"))

def canConstruct(ransomNote: str, magazine: str) -> bool:
        hash_table = {}
        count = 0
        for i in ransomNote:
                count +=1
                hash_table[i] = count

        print(hash_table)
canConstruct("aia", "bb")