"""
    leetcode: canIWIN
"""
# def canIWin(maxChoosableInteger, desiredTotal):
#         """
#         :type maxChoosableInteger: int
#         :type desiredTotal: int
#         :rtype: bool
#         """
#         if desiredTotal > (maxChoosableInteger * (maxChoosableInteger+1)/2):
#             return False
#         if not desiredTotal % (maxChoosableInteger+1):
#             return False
#         chooselist = range(1, maxChoosableInteger+1)
#
#         def win(clist, des):
#             if clist[-1] >= des:
#                 return True
#             else:
#                 res = []
#                 for i in range(len(clist)):
#                     alist = clist[:i] + clist[i+1:]
#                     ades = des - clist[i]
#                     res.append(not win(alist, ades))
#                 dd = not (False in res)
#                 return dd
#         return win(chooselist, desiredTotal)
#
# print canIWin(20, 55)

"""
    leetcode: maxSubArray
"""
# def maxSubArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     maxsum = org = 0
#     sum_temp = 0
#     for num in nums:
#         if org+num > 0:
#             org += num
#             maxsum = max(org, maxsum)
#         else:
#             org = 0
#     return maxsum
#
# print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# test = [12, 121]
# length = len(test)
# for i in range(length):
#     test[i] = str(test[i])
# s = [test[0]]
# for i in range(1, length):
#     temp1 = s[:]
#     temp1.append(test[i])
#     for j in range(i):
#         temp2 = s[:]
#         temp2.insert(j, test[i])
#         if ''.join(temp2) > ''.join(temp1):
#             temp1 = temp2[:]
#     s = temp1[:]
# print ''.join(s)

import os
for i in range(1,33):
    path = '/media/chang/fe3dd8af-5577-42cb-95fb-4bd30a47cc9e/' \
           '.Trash-1000/files/frames/s' + str(i)
    if os.path.exists(path):
        os.system('rm -r '+path)




