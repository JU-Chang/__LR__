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


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxsum = org = 0
    sum_temp = 0
    for num in nums:
        if org+num > 0:
            org += num
            maxsum = max(org, maxsum)
        else:
            org = 0
    return maxsum

print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
