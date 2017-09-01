# -*- coding:utf-8 -*-
'''
2017/09/02:

My algorithm:
-------------
The most simple and stupid way.


Result:
-------

22 / 23 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:

'''

class Solution(object):

    def findAllIndexes(self, target, l):
        '''
        l = [1, 2, 1, 1]
        target = 1

        return [0, 2, 3]
        '''
        ret = []
        for index, item in enumerate(l):
            if item == target:
                ret.append(index)
        return ret
    
    def checkIfMatch(self, indexes, k):
        '''
        indexes = [0, 2, 3]
        k = 1

        index = 0
            2 - 0 = k?
            3 - 0 = k?
        
        index = 2
            3 - 2 = k?
        '''
        num = len(indexes)
        for i, index in enumerate(indexes):
            candidates = range(i + 1, num)
            for candidate  in candidates:
                if abs(index - indexes[candidate]) <= k:
                    return True
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        skip = []
        for i in nums:
            if i not in skip:
                indexes = self.findAllIndexes(i, nums)
                skip.extend(indexes)
                if self.checkIfMatch(indexes, k):
                    return True
            
        return False