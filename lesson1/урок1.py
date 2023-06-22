# def strcount(s): #O(N**2)
#     for sum in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sum == sub_sym:
#                 counter += 1
#             print( sum, counter)
# strcount('abac')

# def strcount(s):#O(N)
#     dct = {}
#     for sum in s:
#         dct[sum] = dct.get(sum, 0) + 1
#
#     for key, value in dct.items():
#         print(key, value)
#
# strcount('aaabcd')
