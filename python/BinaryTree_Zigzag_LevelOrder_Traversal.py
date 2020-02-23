# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        list_all = []
        level_list = deque()
        
        nodes = deque([root, None]) # None is to seperate from other levels
        if_from_left = True
        while len(nodes) > 0:
            curr_node = nodes.popleft()
            
            # check if current node is empty
            if curr_node:
                # get all childs
                if if_from_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                # check if left child is empty, then pass it to nodes
                if curr_node.left:
                    nodes.append(curr_node.left)
                # check if right child is empty, then pass it to nodes
                if curr_node.right:
                    nodes.append(curr_node.right)
            else:
                # append the list to list_all 
                list_all.append(level_list)
                # Add none to nodes
                if len(nodes) > 0:
                    nodes.append(None)
                # clear level list before move to next level
                level_list = deque()
                # change direction 
                if_from_left = not if_from_left
                
        return list_all