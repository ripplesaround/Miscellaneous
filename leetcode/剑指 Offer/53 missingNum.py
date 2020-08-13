# coding=utf-8

"""
Author: ripples
Email: ripplesaround@sina.com

date: 2020/8/13 10:05
desc:
"""
import json
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arraylen = len(nums)
        if arraylen>1:
            n = arraylen + 1
            start = 0
            end = n - 2
            while True:
                if start >= end:
                    break
                mid =int( (start + end)/2 )
                if nums[mid] == mid:
                    start = mid+1
                else:
                    end = mid
                # print(start,end)
            # return start
            if nums[start] > start:
                return start
            else:
                return start + 1
        else:
            if nums[0] == 1:
                return 0
            else:
                return 1

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)

            ret = Solution().missingNumber(nums)
            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()