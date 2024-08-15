# # def mergeAlternately( word1: str, word2: str) -> str:
# #         i , j = 0, 0
# #         while i < len(word1) and j < len(word2):
# #             ans = i , j == word1[i], word2[2]
# #             print(ans)
# # mergeAlternately("ab", "pqrs")

# def count_occurrences(arr):
#     # Initialize an empty hash table (dictionary)
#     hash_table = {}
#     maximum = max(arr)

#     # Iterate through each element in the array
#     for element in arr:
#         # If the element is already in the hash table, increment its count
#         if element in hash_table:
#             hash_table[element] += 1
#         # If the element is not in the hash table, add it with a count of 1
#         else:
#             hash_table[element] = 1
    
#     ans = hash_table[maximum]

#     return hash_table

# # Example usage:
# arr = [3,2,3]
# occurrences = count_occurrences(arr)
# print(occurrences)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

def count_occurrences(arr):
    # Initialize an empty hash table (dictionary)
    hash_table = {}

    # Iterate through each element in the array
    for element in arr:
        # If the element is already in the hash table, increment its count
        if element in hash_table:
            hash_table[element] += 1
        # If the element is not in the hash table, add it with a count of 1
        else:
            hash_table[element] = 1

    # Find the key with the highest value in the hash table
    most_occurrences = max(hash_table, key=hash_table.get)

    return hash_table, most_occurrences

# Example usage:
arr = [2,2,1,1,1,2,2]
occurrences, most_occurrences = count_occurrences(arr)
# print(occurrences)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
print(most_occurrences)  # Output: 4
