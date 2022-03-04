# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        q = collections.deque()
        q.append(root)
        count = 0
        backTrack = False
        while q:
            current = q.pop()
            if not backTrack:
                while current:
                    q.append(current)
                    current = current.left
            if not backTrack:
                current = q.pop()
            backTrack = True
            count += 1
            if count == k:
                return current.val
            if current.right:
                backTrack = False
                q.append(current.right)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
