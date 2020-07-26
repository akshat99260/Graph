# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:05:33 2020

@author: Akshat Jain
"""

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjancyList = []
        self.visited = False
        self.predecessor = None
        
class Depth_First_Search(object):
    def dfs(self,startnode):
        startnode.visited = True
        print("%s"%startnode.name)
        
        for n in startnode.adjancyList:
            if not n.visited:
                self.dfs(n)
                
if __name__ == "__main__":
                
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    
    node1.adjancyList.append(node2)
    node1.adjancyList.append(node3)
    node2.adjancyList.append(node4)
    node3.adjancyList.append(node5)
    node2.adjancyList.append(node6)
    
    if __name__ ==  "__main__":
        d = Depth_First_Search()
        d.dfs(node1)