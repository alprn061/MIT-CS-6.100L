# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10)) 
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))) 
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))) 
# print(tree1)
# print(f"get left - right : {tree1.get_left_child().get_right_child().get_left_child()}") # 2
# print(f"get right : {tree1.get_right_child()}") # 6

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree == None:
        return -1
    else:
        return 1 + max(find_tree_height(tree.get_left_child()), find_tree_height(tree.get_right_child()))

# max heap comparator 
def compare_funcX(child_value, parent_value):
 if child_value < parent_value:
    return True
 return False

# min heap comparator 
def compare_funcN(child_value, parent_value):
 if child_value > parent_value:
    return True
 return False

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is None:
       return True

    #left node
    left = tree.get_left_child()
    # right  node
    right = tree.get_right_child()

    if left is not None:
       # compare left node against parent
        if not compare_func(left.get_value(), tree.get_value()):
          return False
        if not is_heap(left, compare_func):
            return False
    if right is not None:
       if not compare_func(right.get_value(), tree.get_value()):
          return False
       if not is_heap(right, compare_func):
          return False
    return True
    
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    pass