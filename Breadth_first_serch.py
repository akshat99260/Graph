# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:33:10 2020

@author: Akshat Jain
"""

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjancyList = []
        self.visited = False
        self.predecessor = None
        
class Breadth_first_search(object):
    def bfs(self ,startnode):
        Queue =[]
        startnode.visited =True
        Queue.append(startnode)
        
        while Queue:
            actualnode = Queue.pop(0)
            print("%s" %actualnode.name , end = " ")
            
            for n in actualnode.adjancyList:
                if not n.visited:
                    n.visited = True
                    Queue.append(n)

if __name__ == "__main__":
         
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    
    node1.adjancyList.append(node2)
    node2.adjancyList.append(node3)
    node3.adjancyList.append(node4)
    node4.adjancyList.append(node5)
    node5.adjancyList.append(node6)
    
    b = Breadth_first_search()
    b.bfs(node1)

            
        