#1Q Implement Binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        newNode = TreeNode(val)
        if self.root is None:
            self.root = newNode
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if currNode.left is None:
                    currNode.left = newNode
                    break
                else:
                    queue.append(currNode.left)
                if currNode.right is None:
                    currNode.right = newNode
                    break
                else:
                    queue.append(currNode.right)
    def inorderTraversal(self, node):
        if node:
            self.inorderTraversal(node.left)
            print(node.val, end=" ")
            self.inorderTraversal(node.right)
    def preorderTraversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
    def postorderTraversal(self, node):
        if node:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            print(node.val, end=" ")
# Testing the program
if __name__ == "__main__":
    binaryTree = BinaryTree()
    elements = list(map(int,input("enter the list of elements: ").split()))

    for element in elements:
        binaryTree.insert(element)

    print("Inorder Traversal:")
    binaryTree.inorderTraversal(binaryTree.root)
    print()

    print("Preorder Traversal:")
    binaryTree.preorderTraversal(binaryTree.root)
    print()

    print("Postorder Traversal:")
    binaryTree.postorderTraversal(binaryTree.root)
    print()



#2Q Find height of a given tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Height of tree is %d" % (maxDepth(root)))
 

#3Q Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root:
        print(root.data, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=" ")
        in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data, end=" ")
# Constructing the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Pre-order traversal:")
pre_order_traversal(root)
print("\n")
print("In-order traversal:")
in_order_traversal(root)
print("\n")
print("Post-order traversal:")
post_order_traversal(root)
print("\n")


#4Q Function to print all the leaves in a given binary tree

class Node:  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printLeafNodes(root: Node) -> None:   
    if (not root):
        return   
    if (not root.left and
        not root.right):
        print(root.data,
              end = " ")
        return  
    if root.left:
        printLeafNodes(root.left)   
    if root.right:
        printLeafNodes(root.right)
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
    printLeafNodes(root)


#5Q Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,start):
        visited = set()
        queue = [start]
        result = []
        while queue:
            node = queue.pop()
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue += self.graph[node]
        return result
    def DFS(self,start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node)
                stack += reversed(self.graph[node])
            return result
if __name__ == "__main__":
    g = graph()
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)
    print("bfs traversal: ", g.BFS(2))
    print("dfs traversal: ", g.DFS(2))


#6Q Find sum of all left leaves in a given Binary Tree

class Node:
    # Constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
def leftLeavesSum(root):    
    res = 0
    if root is not None:     
        if isLeaf(root.left):
            res += root.left.key
        else:          
            res += leftLeavesSum(root.left)       
        res += leftLeavesSum(root.right)
    return res
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)       
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))


#7Q Find sum of all nodes of the given perfect binary tree

def SumNodes(l):
     # no of leaf nodes
    leafNodeCount = pow(2, l - 1)
 # list of vector to store nodes of  
    vec = [[] for i in range(l)]
    # store the nodes of last level
    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)    
    for i in range(l - 2, -1, -1):
        k = 0  
        while (k < len(vec[i + 1]) - 1):            
            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2
    Sum = 0    
    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]
 
    return Sum
# Driver Code
if __name__ == '__main__':
    l = 3
 
    print(SumNodes(l))


#8Q Count subtress that sum up to a given value x in a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def count_subtree_sum(root, target_sum):
    def search_subtree(node, target):
        if not node:
            return 0       
        count = (node.val == target)
        count += search_subtree(node.left, target - node.val)
        count += search_subtree(node.right, target - node.val)
        return count
    if not root:
        return 0
    # Count the number of subtrees with the given sum using DFS
    count = search_subtree(root, target_sum)
    # Recursively count subtrees in left and right subtrees
    count += count_subtree_sum(root.left, target_sum)
    count += count_subtree_sum(root.right, target_sum)
    return count
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    target_sum = int(input("enter the target sum: "))
    # Count the number of subtrees with the given sum
    num_subtrees = count_subtree_sum(root, target_sum)
    print("Number of subtrees with sum equal to", target_sum, "is", num_subtrees)


#9Q Find maximum level sum in Binary Tree

from collections import deque
class Node:
   def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None
# Function to find the maximum sum
def maxLevelSum(root):
    if (root == None):
        return 0
    result = root.data
    q = deque()
    q.append(root)  
    while (len(q) > 0):
        count = len(q)
        sum = 0
        while (count > 0):
            temp = q.popleft()
            sum = sum + temp.data
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)                
            count -= 1   
        result = max(sum, result)
    return result
# Driver code
if __name__ == '__main__':
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)     
    print("Maximum level sum is", maxLevelSum(root))
 

#10Q Print the nodes at odd levels of a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
def printOddNodes(root, isOdd = True):
# If empty tree
    if (root == None):
        return
    if (isOdd):
        print(root.data, end = " ")
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)

















