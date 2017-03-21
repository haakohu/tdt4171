class Tree:
  
  def __init__(self,value=None):
    self.childs = []
    self.is_leaf = False
    self.variable = None # Index of the element in the training set
    if value != None:
      self.is_leaf = True
    self.value = value # Value for the node if the tree is a leaf node.


  def add_child(self,tree):
    self.childs.append(tree)

  def count_trees(self):
    count = 1
    for i in self.childs:
      count += i.count_trees()
    return count

