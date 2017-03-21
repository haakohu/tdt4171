# Decision tree for boolean variables
from math import log
from tree import Tree
from copy import deepcopy
from random import random
training_data = open('training.txt','r')

#  each row describes the object, 1...N-1 = attributes, N=object class 
read_to_matrix = lambda data: [ [int(x.strip()) for x in line.split()] for line in data]
examples = read_to_matrix(training_data)
training_data.close()
N_attributes = len(examples[0])-1
attributes = [x for x in range(0,N_attributes)]
# q: probability, the entropy function from page 704
def B(q):
  if q==0 or q ==1:
    return 0
  return -(q*log(q,2) + (1-q) *log(1-q,2))

# get positive and negative outcomes when attribute i is in values.
def get_occurences(examples, i, values):
  p = 0
  n = 0
  for row in examples:
    if row[i] in values:
      if row[-1] == 2:
        p+= 1
      else:
        n += 1
  return p, n

# Positive and negative outcomes in the set, 1=False, 2=True
p,n = get_occurences(examples,0,[1,2])


# Expected entropy remaining after testing attribute i
def remainder(examples,i):
  result = 0
  for k in [1,2]:
    p_k, n_k = get_occurences(examples,i,[k])
    result += ((p_k+n_k) / (p+n)) * B(p_k/(p_k+n_k))

  return result

# The importance function 
Gain = lambda i,examples: B(p/(p+n)) - remainder(examples,i)
random_importance = [random() for i in range(N_attributes)]
Gain_random = lambda i,examples: random_importance[i]

# Returns the attribute i with highest priority / information gain
def find_max_attribute(attributes,examples):
  values = [Gain(i,examples) for i in attributes] # Change Gain function to differentiate the importance function
  return attributes[values.index(max(values))]


# Returns examples where attribute i = value
def get_examples_copy(i,value,examples):
  new_exampels = []
  for row in examples:
    if row[i] == value:
      new_exampels.append(row)
  return new_exampels

# Returns the plurality of the values in examples
def plurality_tree(examples):
  N = len(examples)
  s = 0
  for row in examples:
    s += row[-1]
  s /= N
  if s >=1.5:
    return Tree(2)
  return Tree(1)

# Check if a set of examples is of the same class 
def check_same_class(examples):
  count = 0
  for row in examples:
    if row[-1] == 1:
      count += 1
  return count == 0 or count == len(examples)

# Algorithm from page 702, returns a trained tree from the examples
def decision_tree_learning(examples,unused_attributes, parent_examples):
  if len(examples) == 0:
    return plurality_tree(parent_examples)
  if check_same_class(examples):
    if examples[0][-1] == 2:
      return Tree(2)
    return Tree(1)
  if len(unused_attributes) == 0:
    return plurality_tree(examples)
  attributes = deepcopy(unused_attributes)
  i = find_max_attribute(unused_attributes,examples)
  attributes.remove(i)
  tree = Tree()
  tree.variable = i
  for value in [1,2]:
    exs = get_examples_copy(i,value,examples)
    subtree = decision_tree_learning(exs,attributes,parent_examples)
    tree.add_child(subtree)
  return tree

tree = decision_tree_learning(examples,attributes,examples)


# Classifies a row with the given tree.
def classify(tree,row):
  value = row[tree.variable] 
  new_tree = None
  if value == 1:
    new_tree = tree.childs[0]
  elif value == 2:
    new_tree = tree.childs[1]
  if new_tree.is_leaf:
    return new_tree.value
  else:
    return classify(new_tree,row)

# Test the tree on the given data,
def test(tree):
  test_data = open('test.txt')
  test_examples = read_to_matrix(test_data)
  test_data.close()
  correct = 0
  N = len(test_examples)
  for row in test_examples:
    if classify(tree,row) == row[-1]:
      correct += 1

  print(correct/N)
test(tree)