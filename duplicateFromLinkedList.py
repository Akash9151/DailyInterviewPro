
# Given a linked list, remove all duplicate values from the linked list.

# For instance, given 1 -> 2 -> 3 -> 3 -> 4, then we wish to return the linked list 1 -> 2 -> 4.



class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    if not self.next:
      return str(self.val)
    return str(self.val) + " " + str(self.next)

class Solution(object):
  def deleteDuplicates(self, node):
      previus = node
      current = node
      while(True):
          if(current.next == None):
              break
          searcher = current.next
          while(True):
              if( searcher.next == None):
                  break
              elif(current.val == searcher.val):
                  current = previus
                  current.next = searcher.next
                  searcher = searcher.next
              else:
                  searcher = searcher.next
          previus = current
          current = current.next


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
# 1 2 3 3 4
Solution().deleteDuplicates(n)
print(n)
# 1 2 4
